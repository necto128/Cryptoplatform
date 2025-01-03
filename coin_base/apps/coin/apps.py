from django.apps import AppConfig


# import asyncio
# from apps.coin.kafka import consume_messages

class CoinConfig(AppConfig):
    """CoinConfig."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.coin"

    def ready(self):
        """Ready Option."""
        ...
        # loop = asyncio.get_event_loop()
        # loop.create_task(consume_messages())
