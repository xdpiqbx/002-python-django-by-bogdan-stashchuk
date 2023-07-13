from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def index(request: WSGIRequest) -> HttpResponse:
    # print(request)
    return HttpResponse("Hello from the Shop app")
