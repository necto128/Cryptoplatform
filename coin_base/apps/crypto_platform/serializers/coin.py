from rest_framework import serializers

from apps.coin.models import PriceHistory, Directive


class PriceHistorySerializer(serializers.ModelSerializer):
    """Serializer for PriceHistory model."""

    class Meta:
        """Meta options."""

        model = PriceHistory
        fields = [
            'value',
            'timestamp'
        ]


class DirectiveSerializer(serializers.ModelSerializer):
    """Serializer for Directive model."""

    class Meta:
        """Meta options."""

        model = Directive
        fields = [
            'key',
            'symbol',
            'name',
            'is_active'
        ]


class ChoiceDirectiveSerializer(serializers.ModelSerializer):
    """Serializer for Directive model."""

    class Meta:
        """Meta options."""

        model = Directive
        fields = [
            'key',
            'is_active'
        ]
