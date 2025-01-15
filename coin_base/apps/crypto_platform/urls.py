from apps.crypto_platform.view.view_subscription import SubscriptionDirectiveView
from django.urls import path
urlpatterns = [
    path("subscription/", SubscriptionDirectiveView.as_view(), name="subscription"),
]
