import asyncio
import json
import os

from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError
from asgiref.sync import sync_to_async
from dotenv import load_dotenv

load_dotenv()


async def consume_messages():
    """Asynchronously consumes messages from a Kafka topic and processes them."""
    from apps.coin.models import Directive, PriceHistory
    consumer = AIOKafkaConsumer(
        os.getenv("KAFKA_QUEUE"),
        bootstrap_servers=f'{os.getenv("KAFKA_HOST")}:{os.getenv("KAFKA_PORT")}',
        group_id=os.getenv("GROUP_ID"),
        auto_offset_reset='earliest'
    )
    while True:
        try:
            await consumer.start()  # Try to connect
            break
        except KafkaConnectionError:
            await asyncio.sleep(30)

    try:
        while True:
            msg = await consumer.getone()
            message = json.loads(msg.value.decode('utf-8'))
            directive = await sync_to_async(Directive.objects.get)(key=message.get('key'))
            directive.price24h = message.get('p24h')
            await sync_to_async(directive.save)()
            await sync_to_async(PriceHistory.objects.create)(
                directive=directive,
                value=message.get('value')
            )
    finally:
        if consumer:
            await consumer.stop()
