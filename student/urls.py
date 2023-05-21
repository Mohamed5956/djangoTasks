from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='liststudent'),
    path('create', create, name='createstudent'),
    path('update/<int:id>', update, name='updatestudent'),
    path('delete/<int:id>', delete, name='deletestudent')
]
