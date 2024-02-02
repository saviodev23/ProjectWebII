from .views.views_servico import add_servico, editar_servico, remover_servico, confirmar_remocao_servico, detalhes_servico
from .views.views_agenda import fazer_agendamento_pelo_profissional, etapa_de_agendamento, listar_agendamentos_cliente, listar_agendamentos, fazendo_agendamento_pelo_cliente, selecione_profissional_para_agendamento
from django.urls import path

urlpatterns = [
    #Agendamento
    path('etapa/agendamento/<int:servico_id>', etapa_de_agendamento, name="etapa_de_agendamento"),
    path('fazer/agendamento/', fazer_agendamento_pelo_profissional, name="fazer_agendamento_pelo_profissional"),
    path('lista/agendamentos/', listar_agendamentos_cliente, name="listar_agendamentos_cliente"),
    path('listar/agendamentos/', listar_agendamentos, name="listar_agendamentos"),
    # path('fazer/agendamento/cliente/', fazer_agendamento_pelo_cliente, name="fazer_agendamento_pelo_cliente"),
    #Crud serviço
    path('add/servico/', add_servico, name="add_servico"),
    path('editar/servico/<int:servico_id>', editar_servico, name="editar_servico"),
    path('remove/servico/<int:servico_id>', remover_servico, name="remover_servico"),
    path('confirmar/remocao/servico/<int:servico_id>', confirmar_remocao_servico, name="confirmar_remocao_servico"),

    #detalhes do serviço especifico
    path('detalhes/servico/<int:servico_id>', detalhes_servico, name="detalhes_servico"),
    #Fazer agendamento pelo cliente
    path('selecione/profissional/', selecione_profissional_para_agendamento, name="selecione_profissional_para_agendamento"),
    path('fazendo/agendamento/', fazendo_agendamento_pelo_cliente, name="fazendo_agendamento_pelo_cliente"),


    #fazer requisição AJAX para horarios disponiveis
    # path('get/horarios/disponiveis/', get_horarios_disponiveis, name='get_horarios_disponiveis'),
]