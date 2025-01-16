from rest_framework import serializers

from apps.crypto_platform.models import Order
from apps.user.serializers.wallet import CryptoWalletSerializer


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""
    wallet = CryptoWalletSerializer()

    class Meta:
        """Meta options."""
        model = Order
        fields = ["order_type", "currency", "amount", "price", "created_at", "wallet"]
