from django.contrib import admin
from django.urls import path
from perfiles.views import *

urlpatterns = [
    path('registro/',registro, name= "registro"),
    path('login/',login_view, name= "login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    ]