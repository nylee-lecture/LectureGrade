from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='score'),
]