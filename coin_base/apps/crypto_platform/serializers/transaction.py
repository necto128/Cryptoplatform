from rest_framework import serializers

from apps.crypto_platform.models import Order
from apps.crypto_platform.serializers.order import OrderSerializer


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for Transaction model."""
    buy_order = OrderSerializer()
    sell_order = OrderSerializer()

    class Meta:
        """Meta options."""
        model = Order
        fields = ["price", "buy_order", "sell_order", "amount"]
