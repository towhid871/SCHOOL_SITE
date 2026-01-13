# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.member_list, name='member_list'),
    path('', views.MemberListView.as_view(), name='members'),
]