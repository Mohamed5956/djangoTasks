from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='liststaff'),
    path('create', create, name='createstaff'),
    path('update/<int:id>', update, name='updatestaff'),
    path('delete/<int:id>', delete, name='deletestaff')
]
