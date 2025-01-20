from apps.api.admin import admin_site
from apps.coin.models import Directive, PriceHistory

admin_site.register(Directive)
admin_site.register(PriceHistory)
