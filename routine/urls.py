# routine/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoutineListView.as_view(), name='routine_list'),
]