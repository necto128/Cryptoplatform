from rest_framework import serializers

from apps.coin.models import PriceHistory


class PriceHistorySerializer(serializers.ModelSerializer):
    """Serializer for PriceHistory model."""

    class Meta:
        """Meta options."""

        model = PriceHistory
        fields = ['value', 'timestamp']
