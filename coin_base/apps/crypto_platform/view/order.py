from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.crypto_platform.serializers.order import StaticOrderSerializer
from apps.crypto_platform.services import WorkingOrder
from apps.permissions import IsUser


class CreateStaticBuyOrderView(APIView):
    """View for create order buy."""

    permission_classes = [permissions.IsAuthenticated, IsUser]

    @swagger_auto_schema(
        tags=['Order-static'],
        operation_description="Order on buy",
        operation_summary="Order on buy"
    )
    def post(self, request):
        """Create static orders for users."""
        data, user = request.data, request.user
        serializers = StaticOrderSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        if data["order_type"] == "buy":
            services = WorkingOrder(data, user)
            services.get_currency()
            services.get_wallet()
            if services.user_balance.balance < services.price_amount_currency:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"Message": "Insufficient funds to purchase.!"}
                )
            services.user_block()
            services.purchased_crypto()
            services.order_block()
            services.buy_transaction_block()
            return Response(
                status=status.HTTP_201_CREATED,
                data={"Message": "Successfully order!"}
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Have problem with service.!"})


class CreateStaticSellOrderView(APIView):
    """View for create order sell."""

    permission_classes = [permissions.IsAuthenticated, IsUser]

    @swagger_auto_schema(tags=['Order-static'],
                         operation_description="Order on sell",
                         operation_summary="Order on sell"
                         )
    def post(self, request):
        """Create static orders for users."""
        data, user = request.data, request.user
        serializers = StaticOrderSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        if data["order_type"] == "sell":
            services = WorkingOrder(data, user)
            services.get_currency()
            services.main_block()
            if services.working_currency.balance < services.amount_currency:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"Message": "Not enough funds to sell.!"}
                )
            services.calculating_difference()
            services.order_block()
            services.sell_transaction_block()
            return Response(
                status=status.HTTP_201_CREATED,
                data={"Message": "Successfully order!"}
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Message": "Have problem with service.!"})
