from rest_framework import serializers

from apps.user.models import User
# from apps.user.serializers.wallet import WalletBalanceSerializer
from apps.user.models import WalletBalance


class WalletBalanceSerializer(serializers.ModelSerializer):
    """Wallet balance serializer."""

    class Meta:
        """Meta Option."""

        model = WalletBalance
        fields = [
            'currency',
            'balance'
        ]


class UserListSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    balance = WalletBalanceSerializer(many=True, source='wallets.balances')

    class Meta:
        """Meta options."""

        model = User
        fields = [
            "id",
            "type_of_user",
            "email",
            "full_name",
            "is_active",
            "balance"
        ]


class UserActivitySerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        """Meta options."""

        model = User
        fields = [
            "is_active"
        ]
