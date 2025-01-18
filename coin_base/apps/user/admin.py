from django.contrib import admin
from apps.user.models import CryptoWallet, WalletBalance, Subscription, User

admin.site.register(User)
admin.site.register(CryptoWallet)
admin.site.register(WalletBalance)
admin.site.register(Subscription)
