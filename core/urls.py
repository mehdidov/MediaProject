from django.urls import path
from .views import healthcheck, version

urlpatterns = [
    path("healthcheck/", healthcheck),
    path("version/", version),
]
