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

    @classmethod
    def create_subscribe(cls, user, directive):
        """Subscribe to cryptocurrency."""
        for coin_id in directive:
            Subscription.objects.get_or_create(
                user=user,
                directive=Directive.objects.get(key=coin_id)
            )

    @classmethod
    def unsubscribe(cls, user, directive):
        """Unsubscribe from cryptocurrencies."""
        Subscription.objects.filter(user=user.profile, directive__key__in=directive).delete()

    @classmethod
    def get_subscriptions(cls, user):
        """Get all user subscriptions."""
        return user.profile.subscriptions.all()


class CryptoWallet(models.Model):
    """This is the CryptoWallet model. It represents a cryptocurrency wallet for a user."""
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='wallets')
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WalletBalance(models.Model):
    """This model represents the balance of a specific currency in a user's wallet."""
    wallet = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE, related_name='balances')
    currency = models.ForeignKey(Directive, on_delete=models.DO_NOTHING, related_name='wallet_balance')
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)
