from apps.user.view.view import RegisterView, EditPasswordView, DropPasswordView
from django.urls import path

urlpatterns = [
    path("register-user/", RegisterView.as_view(), name="register"),
    path("edit-password/", EditPasswordView.as_view(), name="edit-password"),
    path("drop-password/", DropPasswordView.as_view(), name="drop-password"),
]
