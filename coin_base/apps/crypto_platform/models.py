from django.db import models

from apps.coin.models import Directive
from apps.user.models import CryptoWallet
from django.db.models import Q


class Order(models.Model):
    """Represents a trading order for buying or selling a specific currency."""
    ORDER_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    STATUS_CHOICES = [
        ('open', 'open'),
        ('close', 'close'),
    ]
    wallet = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE, related_name='orders')
    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)


class OrderBook(models.Model):
    """Represents a collection of orders for a specific currency."""
    currency = models.ForeignKey(Directive, on_delete=models.DO_NOTHING, related_name='order_books')
    orders = models.ManyToManyField(Order, related_name='order_books', blank=True)


class Transaction(models.Model):
    """Represents a completed transaction between a buy order and a sell order."""
    buy_order = models.ForeignKey(
        Order, on_delete=models.DO_NOTHING, related_name='buy_transactions', blank=True, null=True)
    sell_order = models.ForeignKey(
        Order, on_delete=models.DO_NOTHING, related_name='sell_transactions', blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_user_transactions(wallet):
        """Method for get list transactions."""
        return Transaction.objects.filter(
            Q(buy_order__wallet=wallet) | Q(sell_order__wallet=wallet)
        )
