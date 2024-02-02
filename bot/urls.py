from django.urls import path
from .views import bot, processar_mensagem


urlpatterns = [
    path('', bot, name= 'bot'),
    #processando mensagens
    path('processar-mensagem/', processar_mensagem, name='processar_mensagem'),
]
