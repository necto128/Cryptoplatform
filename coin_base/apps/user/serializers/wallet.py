from rest_framework import serializers

from apps.user.models import WalletBalance


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
