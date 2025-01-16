from django.urls import path

from apps.user.view.transaction import TransactionHistoryView, OrderHistoryView
from apps.user.view.user_view import RegisterView, EditPasswordView, DropPasswordView
from apps.user.view.wallet_view import BalanceView

urlpatterns = [
    path("register-user/", RegisterView.as_view(), name="register"),
    path("edit-password/", EditPasswordView.as_view(), name="edit-password"),
    path("balance/", BalanceView.as_view(), name="get-balance"),
    path("drop-password/", DropPasswordView.as_view(), name="drop-password"),
    path("transaction-user/", TransactionHistoryView.as_view(), name="transaction-history"),
    path("orders-user/", OrderHistoryView.as_view(), name="orders-history"),
]
