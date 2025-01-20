from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.coin.models import Directive
from apps.crypto_platform.models import Order
from apps.crypto_platform.serializers.coin import DirectiveSerializer, ChoiceDirectiveSerializer
from apps.crypto_platform.serializers.order import OrderAdminSerializer, OrderEditAdminSerializer
from apps.crypto_platform.serializers.user import UserListSerializer, WalletBalanceSerializer, UserActivitySerializer
from apps.permissions import IsAdmin
from apps.user.models import User


class AdminGetCryptView(APIView):
    """Class for admin get and choice crypt activity."""

    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Get list of crypt",
        operation_summary="Get list of crypt"
    )
    def get(self, request):
        """View for get list of crypt."""
        list_directive = Directive.objects.all()
        serializer = DirectiveSerializer(list_directive, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=serializer
        )

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Choice crypt",
        operation_summary="Choice crypt"
    )
    def patch(self, request):
        """View for choice crypt."""
        data = request.data
        directive = get_object_or_404(Directive, key=data["key"])
        serializer = ChoiceDirectiveSerializer(directive, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_200_OK,
            data={"Message": "Successfully!"}
        )


class AdminGetOrderCryptView(APIView):
    """Сlass for the admin to receive modify and delete orders."""

    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Get list of crypt",
        operation_summary="Get list of crypt"
    )
    def get(self, request):
        """View for get list of order."""
        list_order = Order.objects.all()
        serializer = OrderAdminSerializer(list_order, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=serializer
        )

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Edit order",
        operation_summary="Edit order"
    )
    def put(self, request):
        """View for edit order."""
        data = request.data
        order = get_object_or_404(Order, id=data["id"])
        serializer = OrderEditAdminSerializer(order, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if "price" in serializer.validated_data or "amount" in serializer.validated_data:
            transactions = None
            if order.order_type == "buy":
                transactions = order.buy_transactions.first()
            elif order.order_type == "sell":
                transactions = order.sell_transactions.first()
            transactions.amount = data["amount"]
            transactions.price = data["price"]
            transactions.save()
        return Response(
            status=status.HTTP_200_OK,
            data={"Message": "Successfully!"}
        )

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Delete order",
        operation_summary="Delete order"
    )
    def delete(self, request):
        """View for delete order."""
        data = request.data
        order = get_object_or_404(Order, id=data["id"])
        transactions = None
        if order.order_type == "buy":
            transactions = order.buy_transactions.first()
        elif order.order_type == "sell":
            transactions = order.sell_transactions.first()
        transactions.delete()
        order.delete()
        return Response(
            status=status.HTTP_200_OK,
            data={"Message": "Successfully!"}
        )


class AdminUserManagementView(APIView):
    """Class for admin get and choice user activity."""

    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Get list of user",
        operation_summary="Get list of user"
    )
    def get(self, request):
        """View for get list of user."""
        try:
            list_directive = User.objects.filter(type_of_user="user")
            serializer = UserListSerializer(list_directive, many=True).data
            return Response(
                status=status.HTTP_200_OK,
                data=serializer
            )
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=f"{e}")

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Edit balance user",
        operation_summary="Edit balance user"
    )
    def put(self, request):
        """View for edit balance user."""
        try:
            data = request.data
            serializer = WalletBalanceSerializer(data=data["balance"], many=True)
            serializer.is_valid(raise_exception=True)
            user = get_object_or_404(User, id=data["user_id"])
            wallet = user.wallets
            for el in serializer.data:
                wallet.balances.filter(currency=el["currency"]).update(balance=el["balance"])
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=f"{e}")

    @swagger_auto_schema(
        tags=['Administrator'],
        operation_description="Choice active user",
        operation_summary="Choice active user"
    )
    def patch(self, request):
        """View for choice active user."""
        data = request.data
        user = get_object_or_404(User, id=data["user_id"])
        serializer = UserActivitySerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_200_OK,
            data={"Message": "Successfully!"}
        )
