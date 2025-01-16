from django.urls import path

from apps.crypto_platform.view.order import CreateStaticBuyOrderView, CreateStaticSellOrderView
from apps.crypto_platform.view.subscription import SubscriptionDirectiveView
from apps.crypto_platform.view.recommendations import RecommendationsView

urlpatterns = [
    path("create-order-buy/", CreateStaticBuyOrderView.as_view(), name="order-static"),
    path("create-order-sell/", CreateStaticSellOrderView.as_view(), name="order-static"),
    path("subscription/", SubscriptionDirectiveView.as_view(), name="subscription"),
    path("recommendations/", RecommendationsView.as_view(), name="recommendations"),
]
