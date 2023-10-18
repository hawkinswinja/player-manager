from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def status(request):
    return JsonResponse({"status": "success"}, status=200)
