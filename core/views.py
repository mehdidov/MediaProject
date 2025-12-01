from django.shortcuts import render
from django.http import JsonResponse

def healthcheck(request):
    return JsonResponse({"status": "ok"})

def version(request):
    return JsonResponse({"version": "1.0.0"})

def ping(request):
    return JsonResponse({"message": "pong"})

