from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.crypto_platform.models import Transaction
from apps.crypto_platform.serializers.order import OrderSerializer
from apps.crypto_platform.serializers.transaction import TransactionSerializer
from apps.permissions import IsUser


class OrderHistoryView(APIView):
    """View for user Order."""

    permission_classes = [permissions.IsAuthenticated, IsUser]

    @swagger_auto_schema(tags=['Transaction'])
    def get(self, request):
        """Return a list of all order user."""
        user = request.user
        list_orders = user.wallets.orders.all()
        serializer = OrderSerializer(list_orders, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class TransactionHistoryView(APIView):
    """View for user transaction."""

    permission_classes = [permissions.IsAuthenticated, IsUser]

    @swagger_auto_schema(tags=['Transaction'])
    def get(self, request):
        """Return a list of all transaction."""
        user = request.user.wallets
        list_transaction = Transaction.get_user_transactions(user)
        serializer = TransactionSerializer(list_transaction, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
