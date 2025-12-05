import logging               
import django                
from django.http import JsonResponse   
from django.conf import settings      

from rest_framework.views import APIView     
from rest_framework.response import Response 
from drf_spectacular.utils import extend_schema  

from .serializers import PingSerializer  
from media.imagekit import send_to_imagekit  

# C'est our voir les potentielles erreurs dans le terminal
logger = logging.getLogger(__name__)



# FONCTIONS SIMPLES (PAS DES CLASSES API)


def health_check(request):
    # Endpoint pour tester que l’API répond correctement

    return JsonResponse({"message": "pong"})


def version(request):
    # Retourne la version de notre API et la version de Django
    return JsonResponse({
        "api_version": settings.API_VERSION,
        "django_version": django.get_version(),
    })



# VUES BASÉES SUR DES CLASSES


class HealthCheckView(APIView):
    # Documentation pour Swagger
    @extend_schema(
        summary="Health Check",
        description="Vérifie que l’API fonctionne bien.",
        responses={200: PingSerializer},   # Montre à Swagger la forme de la réponse
        tags=["core"]
    )
    def get(self, request):
        
        return Response({"message": "pong"})


class PingView(APIView):

    @extend_schema(
        summary="Ping route",
        description="Route utilisée pour tester Swagger.",
        responses={200: PingSerializer},
        tags=["core"]
    )
    def get(self, request):
        return Response({"message": "pong"})


class UploadFileView(APIView):

    # Documentation Swagger pour les uploads
    @extend_schema(
        summary="Upload file to ImageKit.io",
        tags=["upload"],
        request={
            "multipart/form-data": {  # Formulaire avec fichier
                "type": "object",
                "properties": {
                    "file": {"type": "string", "format": "binary"}  
                },
                "required": ["file"]  # Fichier requis
            }
        },
        responses={200: dict}
    )
    def post(self, request):
        # Récupération du fichier upload par Postman ou Swagger
        incoming_file = request.FILES.get("file")

        # Si rien n'a été upload
        if incoming_file is None:
            return Response({"error": "No file uploaded"}, status=400)

        try:
            # Upload du fichier vers ImageKit
            result = send_to_imagekit(incoming_file)
        
        except Exception as exc:

            # Si l'upload ne s'effectue pas et échoue on affiche le message d'erreur
            logger.error(f"Upload failed: {exc}")
            return Response({"error": str(exc)}, status=500)

        
        return Response(result, status=200)
