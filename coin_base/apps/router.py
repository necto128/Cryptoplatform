from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apps.api.urls_auth')),
    path("", include("apps.crypto_platform.urls")),
    path("", include("apps.user.urls")),
]
