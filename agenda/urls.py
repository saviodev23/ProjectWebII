from .views import fazer_agendamento
from django.urls import path

urlpatterns = [
    path('ver_agenda/', fazer_agendamento, name="ver_agenda"),

]