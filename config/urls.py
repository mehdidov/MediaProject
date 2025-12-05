from django.contrib import admin
from django.urls import path, include

# Routes du projet
urlpatterns = [
    # Route pour accéder à l'interface d'administration Django
    path("admin/", admin.site.urls),

    # Route qui inclut les URL définies dans l'application core
    path("", include("core.urls")),
    

]
