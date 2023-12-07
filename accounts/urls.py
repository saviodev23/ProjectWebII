from .views import register, minha_conta, alterar_dados
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('accounts/register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('minha/conta/', minha_conta, name="minha_conta"),
    path('alterar/dados/', alterar_dados, name='alterar_dados')
]