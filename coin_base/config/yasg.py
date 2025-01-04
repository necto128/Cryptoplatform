from django.urls import include
from django.urls import re_path, path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Products API",
        default_version="v1",
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="TeamStone@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    patterns=[path("api/", include("apps.router"))],
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger_ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
