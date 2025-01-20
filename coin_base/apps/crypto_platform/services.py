from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from apps.coin.models import Directive
from apps.crypto_platform.models import OrderBook, Order
from apps.crypto_platform.models import Transaction
from apps.crypto_platform.serializers.order import OrderAdminSerializer
from apps.crypto_platform.serializers.transaction import TransactionSerializer
from apps.crypto_platform.serializers.user import UserListSerializer
from apps.user.models import User
from apps.user.models import WalletBalance


class WorkingOrder:
    """WorkingOrder services."""

    def __init__(self, data, user):
        """WorkingOrder services initialization."""
        self.user = user
        self.id_currency = data["currency"]
        self.order_type = data["order_type"]
        self.amount = data["amount"]
        self.currency = None
        self.main_currency = None
        self.last_price = None
        self.user_balance = None
        self.price_amount_currency = None
        self.purchased_crypt = None
        self.user_wallet = None
        self.amount_currency = None
        self.currency = None
        self.usdt = None
        self.working_currency = None
        self.order = None

    def calculating_difference(self):
        """Get calculating difference."""
        self.working_currency.balance -= self.amount_currency
        self.usdt.balance += self.amount_currency * self.last_price
        self.working_currency.save()
        self.usdt.save()

    def main_block(self):
        """Block get wallet and user."""
        self.user_wallet = self.user.wallets
        self.main_currency = self.user_wallet.balances.filter(currency__key__in=[self.id_currency, 825])
        self.usdt = self.main_currency.filter(currency__key=825).first()
        self.working_currency = self.main_currency.filter(currency__key=self.id_currency).first()
        if self.working_currency is None:
            WalletBalance.objects.create(wallet=self.user_wallet, currency=self.currency, balance=0)
        self.amount_currency = self.amount

    def purchased_crypto(self):
        """Get purchased crypto."""
        if self.purchased_crypt is None:
            WalletBalance.objects.create(
                wallet=self.user_wallet,
                currency=self.currency,
                balance=self.amount
            )
        else:
            self.purchased_crypt.balance += self.amount
            self.purchased_crypt.save()

    def get_currency(self):
        """Get currency price."""
        self.currency = Directive.objects.get(key=self.id_currency)
        self.last_price = self.currency.price_history.latest('timestamp').value

    def get_wallet(self):
        """Block get wallet user."""
        self.user_wallet = self.user.wallets
        self.user_balance = self.user_wallet.balances.get(currency__symbol="USDT")
        self.price_amount_currency = self.amount * self.last_price

    def user_block(self):
        """Block user."""
        self.user_balance.balance -= self.price_amount_currency
        self.user_balance.save()
        self.purchased_crypt = self.user_wallet.balances.filter(currency__key=self.id_currency).first()

    def order_block(self):
        """Block order."""
        order_book = OrderBook.objects.get(currency=self.currency)
        self.order = Order.objects.create(
            order_type=self.order_type,
            currency=order_book.currency.symbol,
            wallet=self.user_wallet,
            amount=self.amount,
            price=self.last_price,
            status="close"
        )
        order_book.orders.add(self.order)

    def buy_transaction_block(self):
        """Transaction order."""
        Transaction.objects.create(
            buy_order=self.order,
            price=self.order.price,
            amount=self.amount
        )

    def sell_transaction_block(self):
        """Transaction order."""
        Transaction.objects.create(
            sell_order=self.order,
            price=self.order.price,
            amount=self.amount
        )


class AdministrationWork:
    """Class for working with Administration func."""

    @staticmethod
    def get_list_orders():
        """Return list all orders."""
        try:
            list_order = Order.objects.all()
            serializer = OrderAdminSerializer(list_order, many=True).data
            return Response(
                status=status.HTTP_200_OK,
                data=serializer
            )
        except Exception:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def get_list_user():
        """Return list all user."""
        try:
            list_directive = User.objects.filter(type_of_user="user")
            serializer = UserListSerializer(list_directive, many=True).data
            return Response(
                status=status.HTTP_200_OK,
                data=serializer
            )
        except Exception:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def get_list_transactions_user(user_id: int):
        """"Return a list of all transaction user."""
        user = get_object_or_404(User, id=user_id)
        try:
            wallet = user.wallets
            list_transaction = Transaction.get_user_transactions(wallet)
            serializer = TransactionSerializer(list_transaction, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        except Exception:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
