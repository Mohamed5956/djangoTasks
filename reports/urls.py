from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('liststudent',list_students),
    path('liststaff',list_staff),
    path('links',links)
]
