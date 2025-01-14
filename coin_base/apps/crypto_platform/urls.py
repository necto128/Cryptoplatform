from apps.crypto_platform.view.order import CreateStaticBuyOrderView, CreateStaticSellOrderView
from django.urls import path

urlpatterns = [
    path("create-order-buy/", CreateStaticBuyOrderView.as_view(), name="order-static"),
    path("create-order-sell/", CreateStaticSellOrderView.as_view(), name="order-static"),
]
