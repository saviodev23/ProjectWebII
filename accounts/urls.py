from.views.views import register, minha_conta, alterar_dados, remover_conta
from.views.view_admin import listar_e_cadastrar_usuarios, editar_usuario, remover_usuario, confirmar_remocao_usuario
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    #cadastroForaDoSistema
    path('login/', LoginView.as_view(), name="login"),
    path('accounts/register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #AlterarDadosUsuario
    path('minha/conta/', minha_conta, name="minha_conta"),
    path('alterar/dados/', alterar_dados, name='alterar_dados'),
    path('remover/conta/<int:user_id>', remover_conta, name="remover_conta"),
    # path('confirmar/remocao/conta/<int:user_id>', confirmar_remocao_conta, name="confirmar_remocao_conta"),

    #CadastroDentroDoSistema__Administrador
    path('listar/usuarios/', listar_e_cadastrar_usuarios, name="listar_e_cadastrar_usuarios"),
    path('editar/usuario/<int:user_id>', editar_usuario, name="editar_usuario"),
    path('remover/usuario/<int:user_id>', remover_usuario, name="remover_usuario"),
    path('confirmar/remocao/usuario/<int:user_id>', confirmar_remocao_usuario, name="confirmar_remocao_usuario"),

    #recuperação de senha   path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]