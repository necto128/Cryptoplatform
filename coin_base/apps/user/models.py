from django.contrib.auth.models import User
from django.db import models

from apps.coin.models import Directive


class Profile(models.Model):
    """This is the Profile model. It represents the profile of a registered user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


class Subscription(models.Model):
    """Subscription model to track user subscriptions to cryptocurrencies."""
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='subscriptions')
    directive = models.ForeignKey(Directive, on_delete=models.DO_NOTHING, related_name='directive_subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta Option."""
        unique_together = ('user', 'directive')

    def create_subscribe(self, directive):
        """Subscribe to cryptocurrency."""
        Subscription.objects.get_or_create(user=self, directive=directive)

    def unsubscribe(self, directive):
        """Unsubscribe from cryptocurrencies."""
        Subscription.objects.filter(user=self, directive__in=directive).delete()

    def get_subscriptions(self):
        """Get all user subscriptions."""
        return self.subscriptions.all()


class CryptoWallet(models.Model):
    """This is the CryptoWallet model. It represents a cryptocurrency wallet for a user."""
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='wallets')
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WalletBalance(models.Model):
    """This model represents the balance of a specific currency in a user's wallet."""
    wallet = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE, related_name='balances')
    currency = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)
