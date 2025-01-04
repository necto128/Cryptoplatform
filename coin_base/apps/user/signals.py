from django.contrib.auth.models import User
from apps.user.models import Profile, CryptoWallet
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    """Create new user_settings for new user."""
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
        uid = str(uuid.uuid4())
        while True:
            if not CryptoWallet.objects.get(uid=uid):
                CryptoWallet.objects.create(
                    profile=profile,
                    address=uid.replace("-", "")
                )
                break
            uid = str(uuid.uuid4())
