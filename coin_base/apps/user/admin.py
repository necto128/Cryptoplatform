from django.contrib import admin
from apps.user.models import CryptoWallet, Profile, WalletBalance, Subscription

admin.site.register(CryptoWallet)
admin.site.register(Profile)
admin.site.register(WalletBalance)
admin.site.register(Subscription)
