from django.urls import include
from django.urls import path

from config.yasg import urlpatterns as swagger_urls

urlpatterns = [

    path("api/", include("apps.router")),
]
urlpatterns += swagger_urls
