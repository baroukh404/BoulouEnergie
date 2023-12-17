from django.contrib import admin
from django.urls import path, include
from . import views

device = views.SmartPlug("bfbbe603f37b831375vgzq")

urlpatterns = [
    path('', views.smart_plug),
    path('<str:switch>', views.smart_plug),
    path('<str:deviceId>', views.smart_plug)
]
