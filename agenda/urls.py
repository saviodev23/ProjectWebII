from .views.views_servico import add_servico, editar_servico, remover_servico, confirmar_remocao_servico, detalhes_servico, add_imagem_servico, editar_imagem_servico, remover_imagem_servico, confirmar_remocao_imagem_servico
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

    #Crud imagem de servico
    path('add/imagem/servico/' , add_imagem_servico, name="add_imagem_servico"),
    path('editar/imagem/servico/<int:img_servico_id>', editar_imagem_servico, name="editar_imagem_servico"),
    path('remover/imagem/servico/<int:img_servico_id>', remover_imagem_servico, name="remover_imagem_servico"),
    path('confirmar/remocao/imagem/servico/<int:img_servico_id>', confirmar_remocao_imagem_servico, name="confirmar_remocao_imagem_servico"),

    #detalhes do serviço especifico
    path('detalhes/servico/<int:servico_id>', detalhes_servico, name="detalhes_servico"),

    #Fazer agendamento pelo cliente
    path('selecione/profissional/', selecione_profissional_para_agendamento, name="selecione_profissional_para_agendamento"),
    path('fazendo/agendamento/', fazendo_agendamento_pelo_cliente, name="fazendo_agendamento_pelo_cliente"),

    #fazer requisição AJAX para horarios disponiveis
    # path('get/horarios/disponiveis/', get_horarios_disponiveis, name='get_horarios_disponiveis'),
]