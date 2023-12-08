from .views import agenda
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('ver_agenda/', agenda, name="ver_agenda"),

]