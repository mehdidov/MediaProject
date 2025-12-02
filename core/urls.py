from django.urls import path
from .views import HealthCheckView, VersionView, PingView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("healthcheck/", HealthCheckView.as_view(), name="healthcheck"),
    path("version/", VersionView.as_view(), name="version"),
    path("ping/", PingView.as_view(), name="ping"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc-ui"),
]
