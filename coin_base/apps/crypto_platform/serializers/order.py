from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.coin.models import Directive
from apps.crypto_platform.models import Order
from apps.user.serializers.wallet import CryptoWalletSerializer


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""

    wallet = CryptoWalletSerializer()

    class Meta:
        """Meta options."""

        model = Order
        fields = [
            "order_type",
            "currency",
            "amount",
            "price",
            "created_at",
            "wallet"
        ]


class StaticOrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""

    class Meta:
        """Meta options."""

        model = Order
        fields = [
            "order_type",
            "currency",
            "amount"
        ]

    def validate(self, attrs):
        """Check if the associated Directive is active."""
        currency = attrs.get('currency')
        directive = Directive.objects.filter(key=currency).first()
        if directive and not directive.is_active:
            raise ValidationError('The associated Directive is not active.')
        return attrs


class OrderAdminSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""

    wallet = CryptoWalletSerializer()

    class Meta:
        """Meta options."""

        model = Order
        fields = [
            "id",
            "order_type",
            "currency",
            "amount",
            "price",
            "created_at",
            "wallet",
            "status"
        ]


class OrderEditAdminSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""

    class Meta:
        """Meta options."""

        model = Order
        fields = [
            "id",
            "currency",
            "amount",
            "price",
            "status"
        ]
