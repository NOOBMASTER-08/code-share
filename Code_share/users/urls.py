

from django.contrib import admin
from django.urls import path ,include
from . import views

#from users import indexm.html
urlpatterns = [
    path('', views.user),
]
