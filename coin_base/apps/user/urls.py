from apps.user.view.user_view import RegisterView, EditPasswordView
from apps.user.view.wallet_view import BalanceView
from django.urls import path

urlpatterns = [
    path("register-user/", RegisterView.as_view(), name="register"),
    path("edit-password/", EditPasswordView.as_view(), name="edit-password"),
    path("balance/", BalanceView.as_view(), name="get-balance"),
]
