from apps.api.admin import admin_site
from apps.user.models import CryptoWallet, WalletBalance, Subscription, User

admin_site.register(User)
admin_site.register(CryptoWallet)
admin_site.register(WalletBalance)
admin_site.register(Subscription)
