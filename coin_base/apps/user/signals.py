import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.coin.models import Directive
from apps.user.models import User, CryptoWallet
from apps.user.models import WalletBalance


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    """Create new user_settings for new user."""
    if created:
        uid = str(uuid.uuid4())
        while True:
            if not CryptoWallet.objects.filter(address=uid).first():
                wallet = CryptoWallet.objects.create(
                    user=instance,
                    address=uid.replace("-", "")
                )
                WalletBalance.objects.create(
                    wallet=wallet,
                    currency=Directive.objects.get(key=825),
                )
                break
            uid = str(uuid.uuid4())
