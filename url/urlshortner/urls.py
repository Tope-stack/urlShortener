import imp
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('createshorturl', views.createshorturl, name="createshorturl"),
    path("urlcreated", views.urlcreated, name="urlcreated"),
]