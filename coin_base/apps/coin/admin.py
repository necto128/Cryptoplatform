from django.contrib import admin
from apps.coin.models import Directive, PriceHistory

admin.site.register(Directive)
admin.site.register(PriceHistory)
