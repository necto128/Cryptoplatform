from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.coin.models import Directive


class UserManager(BaseUserManager):
    """Custom user model manager where login is the unique identifiers for authentication instead of usernames."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a 'User' with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a 'User' with superuser (admin) privileges."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model for registered users."""

    TYPE_OF_USER_CHOICES = (
        ("user", "User"),
        ("admin", "Admin"),
        ("analyst", "Analyst")
    )

    type_of_user = models.CharField(max_length=8, choices=TYPE_OF_USER_CHOICES, default="user")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    full_name = models.CharField(max_length=30)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """Str function."""
        return self.email


class Subscription(models.Model):
    """Subscription model to track user subscriptions to cryptocurrencies."""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='subscriptions')
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
        Subscription.objects.filter(user=user, directive__key__in=directive).delete()

    @staticmethod
    def get_subscriptions(user):
        """Get all user subscriptions."""
        return user.subscriptions.all()


class CryptoWallet(models.Model):
    """This is the CryptoWallet model. It represents a cryptocurrency wallet for a user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallets')
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WalletBalance(models.Model):
    """This model represents the balance of a specific currency in a user's wallet."""

    wallet = models.ForeignKey(CryptoWallet, on_delete=models.CASCADE, related_name='balances')
    currency = models.ForeignKey(Directive, on_delete=models.DO_NOTHING, related_name='wallet_balance')
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)
