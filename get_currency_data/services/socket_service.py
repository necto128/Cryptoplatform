import json

import websockets
from aiokafka import AIOKafkaProducer
from resource.websocket_resource import WebSocketResource
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


async def teke_crypto(producer, message_data):
    """Kafka message tagging function for the main service."""
    df = pd.read_csv('crypto_base.csv')
    getting_crypt_info = df[df["id"] == message_data["id"]]
    message = {
        'key': message_data['id'],
        'symbol': getting_crypt_info['symbol'].values[0],
        'name': getting_crypt_info['name'].values[0],
        'value': message_data['p'],
    }
    await producer.send_and_wait(os.getenv('KAFKA_QUEUE'), value=message)


async def crypto_websocket():
    """
    A websocket function that receives data from a third-party service based on
    a subscription message and redirects it to the main service.
    """
    producer = AIOKafkaProducer(
        bootstrap_servers=f"{os.getenv('KAFKA_HOST')}:{os.getenv('KAFKA_PORT')}",
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    await producer.start()
    async with websockets.connect(WebSocketResource.WS_CRYPTO) as websocket:
        print("Websockets connect")
        await websocket.send(json.dumps(WebSocketResource.message_call_5s_normal))
        while True:
            try:
                message = await websocket.recv()
                message_data = json.loads(message).get("d")
                if message_data:
                    await teke_crypto(producer, message_data)
            except websockets.ConnectionClosed:
                print("Websockets connect close")
                await producer.stop()
                break
