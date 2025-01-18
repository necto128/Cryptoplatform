from django.urls import path
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenBlacklistView,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    """Class CustomTokenObtainPairView."""

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request, *args, **kwargs):
        """View for obtaining a pair of access and refresh tokens."""
        return super().post(request, *args, **kwargs)


class CustomTokenVerifyView(TokenVerifyView):
    """Class CustomTokenVerifyView."""

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request, *args, **kwargs):
        """View for verifying a given access token."""
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    """Class CustomTokenRefreshView."""

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request, *args, **kwargs):
        """View for refreshing an access token using a refresh token."""
        return super().post(request, *args, **kwargs)


class CustomTokenBlacklistView(TokenBlacklistView):
    """Class CustomTokenBlacklistView."""

    @swagger_auto_schema(tags=['Authentication'])
    def post(self, request, *args, **kwargs):
        """View for blacklisting a refresh token."""
        return super().post(request, *args, **kwargs)


urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
    path("logout/", CustomTokenBlacklistView.as_view(), name="token_blacklist"),
]
