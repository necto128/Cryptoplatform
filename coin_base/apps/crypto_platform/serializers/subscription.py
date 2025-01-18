from rest_framework import serializers

from apps.coin.models import Directive, PriceHistory


class PriceHistorySerializer(serializers.ModelSerializer):
    """Serializer for PriceHistory model."""

    class Meta:
        """Meta options for PriceHistorySerializer."""

        model = PriceHistory
        fields = ['value', 'timestamp']


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for Directive model to include subscription information."""

    last_price = serializers.SerializerMethodField()

    class Meta:
        """Meta options for SubscriptionSerializer."""

        model = Directive
        fields = ['key', 'symbol', 'price24h', 'last_price']

    def get_last_price(self, obj):
        """Retrieve the last price entry for the given directive."""
        last_price_entry = obj.price_history.order_by('-timestamp').first()
        if last_price_entry:
            return PriceHistorySerializer(last_price_entry).data
        return None


class ListSubscriptionSerializer(serializers.Serializer):
    """Serializer for subscriptions."""

    subscription = serializers.PrimaryKeyRelatedField(
        queryset=Directive.objects.all(),
        many=True
    )
