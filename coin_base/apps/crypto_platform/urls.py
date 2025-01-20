from django.urls import path

from apps.crypto_platform.view.admin import AdminGetCryptView, AdminGetOrderCryptView, AdminUserManagementView
from apps.crypto_platform.view.coin import HistoryCryptView
from apps.crypto_platform.view.order import CreateStaticBuyOrderView, CreateStaticSellOrderView
from apps.crypto_platform.view.recommendations import RecommendationsView
from apps.crypto_platform.view.subscription import SubscriptionDirectiveView

urlpatterns = [
    path("create-order-buy/", CreateStaticBuyOrderView.as_view(), name="order-static"),
    path("create-order-sell/", CreateStaticSellOrderView.as_view(), name="order-static"),
    path("subscription/", SubscriptionDirectiveView.as_view(), name="subscription"),
    path("recommendations/", RecommendationsView.as_view(), name="recommendations"),
    path("history-crypt/<int:crypto_id>/", HistoryCryptView.as_view(), name="crypt-history"),
    path("admins/crypts/", AdminGetCryptView.as_view(), name="admin-crypt"),
    path("admins/order/", AdminGetOrderCryptView.as_view(), name="admin-order"),
    path("admins/user/", AdminUserManagementView.as_view(), name="admin-user"),
]
