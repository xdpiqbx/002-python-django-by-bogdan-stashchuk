from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request: WSGIRequest, course_id: int) -> HttpResponse:
    # path('<int:course_id>', views.single_course, name='single_course'),
    # # Option 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()

    # # Option 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})
