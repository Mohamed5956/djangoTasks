from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', mylogin, name='mylogin'),
    path('register', myregister, name='myregister'),
]
