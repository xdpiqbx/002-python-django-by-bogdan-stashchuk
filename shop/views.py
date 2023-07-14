from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from .models import Course, Category

# Create your views here.
# def index(request: WSGIRequest) -> HttpResponse:
#     # print(request)
#     return HttpResponse("Hello from the Shop app")

# def index(request: WSGIRequest) -> HttpResponse:
#     courses = Course.objects.all()
#     return HttpResponse('<br/>'.join([str(course) for course in courses]))

def index(request: WSGIRequest) -> HttpResponse:
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
