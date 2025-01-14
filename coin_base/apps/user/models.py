from django.contrib.auth.models import User
from django.db import models
from apps.coin.models import Directive

class Profile(models.Model):
    """This is the Profile model. It represents the profile of a registered user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

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

