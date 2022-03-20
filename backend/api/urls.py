from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import api_home

urlpatterns = [
    path('', api_home,name='api_home'),

]
