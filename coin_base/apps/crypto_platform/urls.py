from django.urls import path

from apps.crypto_platform.view.order import CreateStaticBuyOrderView, CreateStaticSellOrderView
from apps.crypto_platform.view.view_subscription import SubscriptionDirectiveView

urlpatterns = [
    path("create-order-buy/", CreateStaticBuyOrderView.as_view(), name="order-static"),
    path("create-order-sell/", CreateStaticSellOrderView.as_view(), name="order-static"),
    path("subscription/", SubscriptionDirectiveView.as_view(), name="subscription"),
]
