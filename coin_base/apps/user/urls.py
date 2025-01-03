from apps.user.view.view import RegisterView, EditPasswordView
from django.urls import path

urlpatterns = [
    path("register-user/", RegisterView.as_view(), name="register"),
    path("edit-password/", EditPasswordView.as_view(), name="edit-password"),
]
