from apps.api.admin import admin_site
from apps.crypto_platform.models import Order, OrderBook, Transaction

admin_site.register(Order)
admin_site.register(OrderBook)
admin_site.register(Transaction)
