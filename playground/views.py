from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseNotAllowed
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World")


def status_check(request):
    if request.method == "GET":
        return JsonResponse({"status": "active"})
    return HttpResponseNotAllowed(["GET"])

