from django.db import models
from apps.coin.models import Directive


class Order(models.Model):
    """Represents a trading order for buying or selling a specific currency."""
    ORDER_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    order_type = models.CharField(max_length=4, choices=ORDER_TYPE_CHOICES)
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=10, default='open')
    created_at = models.DateTimeField(auto_now_add=True)


class OrderBook(models.Model):
    """Represents a collection of orders for a specific currency."""
    currency = models.ForeignKey(Directive, on_delete=models.CASCADE, related_name='order_books')
    orders = models.ManyToManyField(Order, related_name='order_books')


class Transaction(models.Model):
    """Represents a completed transaction between a buy order and a sell order."""
    buy_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='buy_transactions')
    sell_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='sell_transactions')
    price = models.DecimalField(max_digits=20, decimal_places=8)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
