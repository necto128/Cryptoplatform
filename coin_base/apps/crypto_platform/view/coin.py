from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.coin.models import Directive
from apps.crypto_platform.serializers.coin import PriceHistorySerializer


class HistoryCryptView(APIView):
    """View for get history crypt."""

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        tags=['Plotting graphs'],
        operation_description="Get history crypt data",
        operation_summary="Get history crypt data"
    )
    def get(self, request, crypto_id):
        """View for get history crypt for crypto_id."""
        directive_obj = get_object_or_404(Directive, key=crypto_id)
        history_list = PriceHistorySerializer(directive_obj.price_history, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=history_list
        )
