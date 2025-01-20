from django.urls import include, path

from apps.api.admin import admin_site

urlpatterns = [
    path("admin/", admin_site.urls),
    path("", include('apps.api.urls_auth')),
    path("", include("apps.crypto_platform.urls")),
    path("", include("apps.user.urls")),
]
