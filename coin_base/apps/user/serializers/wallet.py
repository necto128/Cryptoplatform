from rest_framework import serializers

from apps.user.models import WalletBalance, CryptoWallet


class WalletBalanceSerializer(serializers.ModelSerializer):
    """Wallet balance serializer."""
    symbol = serializers.SerializerMethodField()

    class Meta:
        """Meta Option."""
        model = WalletBalance
        fields = ['balance', 'symbol']

    def get_symbol(self, obj):
        """Get the symbol of the wallet."""
        return obj.currency.symbol


class CryptoWalletSerializer(serializers.ModelSerializer):
    """Crypto Wallet serializer."""

    class Meta:
        """Meta Option."""
        model = CryptoWallet
        fields = ['address']

    def to_representation(self, instance):
        """Customize the representation of the serialized data."""
        representation = super().to_representation(instance)
        return representation['address']
