from .views import register, minha_conta, alterar_dados, listar_usuarios, editar_usuario, remover_usuario, confirmar_remocao_usuario
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    #cadastroForaDoSistema
    path('login/', LoginView.as_view(), name="login"),
    path('accounts/register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #AlterarDadosUsuario
    path('minha/conta/', minha_conta, name="minha_conta"),
    path('alterar/dados/', alterar_dados, name='alterar_dados'),
    #CadastroDentroDoSistema__Administrador
    path('listar/usuarios/', listar_usuarios, name="listar_usuarios"),
    path('editar/usuario/<int:user_id>', editar_usuario, name="editar_usuario"),
    path('remover/usuario/<int:user_id>', remover_usuario, name="remover_usuario"),
    path('confirmar/remocao/usuario/<int:user_id>', confirmar_remocao_usuario, name="confirmar_remocao_usuario"),
]