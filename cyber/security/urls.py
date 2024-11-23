from django.urls import path
from django.shortcuts import render 
from . import views

urlpatterns = [
    path("",views.test, name="test"),
    path("pagetemoin",views.temoigner, name="temoin")
]
