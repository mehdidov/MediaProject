from django.urls import path
from .views import healthcheck, version, ping

urlpatterns = [
    path("healthcheck/", healthcheck),
    path("version/", version),
    path("ping/", ping),
]
