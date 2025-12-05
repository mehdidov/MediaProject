from django.urls import path
from .views import HealthCheckView, PingView, UploadFileView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


# urlpatterns contient les URL de l'API (les différents endpoints ou routes).

urlpatterns = [
    
    # Vérifie que le site fonctionne en retournant "status: ok"
    path("healthcheck/", HealthCheckView.as_view(), name="healthcheck"),

    # Il vérifie que l’API répond bien et envoie message: pong si c'est le cas
    path("ping/", PingView.as_view(), name="ping"),

    # Sert à envoyer un fichier vers une API comme par exemple l'upload vers ImageKit
    path("upload/", UploadFileView.as_view(), name="upload"),

    # Cela produit un fichier qui décrit l'API en JSON et il est utilisé par Swagger et le Redoc
    path("schema/", SpectacularAPIView.as_view(), name="schema"),

    # C'est une interface avec une documentation qui permet de tester l'API
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    # C'est également une interface avec une documentation
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc-ui",
    ),
]
