from django.urls import path
from . import views  # from current folder import file views.py

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
]
