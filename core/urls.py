from django.urls import path
from .views import HealthCheckView, PingView, UploadFileView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    
    path("healthcheck/", HealthCheckView.as_view(), name="healthcheck"),
    path("ping/", PingView.as_view(), name="ping"),

    
    path("upload/", UploadFileView.as_view(), name="upload"),

    #
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc-ui",
    ),
]
