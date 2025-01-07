import json
import os

from asgiref.sync import sync_to_async
from confluent_kafka import Consumer, KafkaException
from dotenv import load_dotenv

load_dotenv()


async def consume_messages():
    """Asynchronously consumes messages from a Kafka topic and processes them."""
    from apps.coin.models import Directive, PriceHistory
    consumer = Consumer({
        'bootstrap.servers': f'{os.getenv("KAFKA_HOST")}:{os.getenv("KAFKA_PORT")}',
        'group.id': os.getenv("GROUP_ID"),
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([os.getenv("KAFKA_QUEUE")])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            message = json.loads(msg.value().decode('utf-8'))
            directive = await sync_to_async(Directive.objects.get)(key=message.get('key'))
            directive.price24h = message.get('p24h')
            await sync_to_async(directive.save)()
            await sync_to_async(PriceHistory.objects.create)(
                directive=directive,
                value=message.get('value')
            )
    finally:
        consumer.close()
