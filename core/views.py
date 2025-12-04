import logging
import django
from django.http import JsonResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import PingSerializer
from media.imagekit import send_to_imagekit

logger = logging.getLogger(__name__)


def health_check(request):
    return JsonResponse({"message": "pong"})


def version(request):
    return JsonResponse({
        "api_version": settings.API_VERSION,
        "django_version": django.get_version(),
    })


class HealthCheckView(APIView):

    @extend_schema(
        summary="Health Check",
        description="Simple route to verify API availability.",
        responses={200: PingSerializer},
        tags=["core"]
    )
    def get(self, request):
        return Response({"message": "pong"})


class PingView(APIView):

    @extend_schema(
        summary="Ping route",
        description="Used to test the swagger system.",
        responses={200: PingSerializer},
        tags=["core"]
    )
    def get(self, request):
        return Response({"message": "pong"})



class UploadFileView(APIView):

    @extend_schema(
        summary="Upload file to ImageKit.io",
        tags=["upload"],
        request={
            "multipart/form-data": {
                "type": "object",
                "properties": {
                    "file": {"type": "string", "format": "binary"}
                },
                "required": ["file"]
            }
        },
        responses={200: dict}
    )
    def post(self, request):
        incoming_file = request.FILES.get("file")

        if incoming_file is None:
            return Response({"error": "No file uploaded"}, status=400)

        try:
            result = send_to_imagekit(incoming_file)
        except Exception as exc:
            logger.error(f"Upload failed: {exc}")
            return Response({"error": str(exc)}, status=500)

        return Response(result, status=200)
