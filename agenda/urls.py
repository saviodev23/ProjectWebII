from .views.views_servico import add_servico, editar_servico, remover_servico, confirmar_remocao_servico, detalhes_servico
from .views.views_agenda import fazer_agendamento_pelo_profissional, etapa_de_agendamento, listar_agendamentos_cliente, listar_agendamentos, editar_agendamento,concluir_agendamento
from django.urls import path
from ProjectWebII.utils import mostrar_pontos, resgatar_cupon

urlpatterns = [
    #Agendamento
    path('etapa/agendamento/<int:servico_id>', etapa_de_agendamento, name="etapa_de_agendamento"),
    path('fazer/agendamento/', fazer_agendamento_pelo_profissional, name="fazer_agendamento_pelo_profissional"),
    path('lista/agendamentos/', listar_agendamentos_cliente, name="listar_agendamentos_cliente"),
    path('listar/agendamentos/', listar_agendamentos, name="listar_agendamentos"),
    path('editar/agendamento/<int:agendamento_id>', editar_agendamento, name="editar_agendamento"),
    path('concluir/agendamento/<int:agendamento_id>/', concluir_agendamento, name='concluir_agendamento'),
  
    #Crud serviço
    path('add/servico/', add_servico, name="add_servico"),
    path('editar/servico/<int:servico_id>', editar_servico, name="editar_servico"),
    path('remove/servico/<int:servico_id>', remover_servico, name="remover_servico"),
    path('confirmar/remocao/servico/<int:servico_id>', confirmar_remocao_servico, name="confirmar_remocao_servico"),
    #Crud Fidelidade
    path('Fidelidade/<int:user_id>', mostrar_pontos, name="mostrar_pontos"),
    path('Fidelidade/resgatar/<int:user_id>', resgatar_cupon, name="resgatar_cupon"),

    #detalhes do serviço especifico
    path('detalhes/servico/<int:servico_id>', detalhes_servico, name="detalhes_servico"),
]