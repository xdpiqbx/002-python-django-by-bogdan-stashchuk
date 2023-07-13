from django.urls import path
from . import views  # from current folder import file views.py

urlpatterns = [
    path('', views.index, name='index'),
]
