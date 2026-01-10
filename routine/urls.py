# routine/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.routine_list, name='routine_list'),
]