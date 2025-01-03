from django.db import models


class Directive(models.Model):
    """Directive model."""
    key = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

class PriceHistory(models.Model):
    """PriceHistory model."""
    directive = models.ForeignKey(Directive, on_delete=models.CASCADE, related_name='price_history')
    value = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
