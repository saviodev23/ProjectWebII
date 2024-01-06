from .views.views_servico import add_servico, editar_servico, remover_servico, confirmar_remocao_servico, detalhes_servico, listar_servicos
from .views.views_agenda import fazer_agendamento, etapa_de_agendamento
from django.urls import path

urlpatterns = [
    path('etapa/agendamento/<int:servico_id>', etapa_de_agendamento, name="etapa_de_agendamento"),
    path('fazer/agendamento/<int:servico_id>', fazer_agendamento, name="fazer_agendamento"),
    #Crud serviço
    path('listar/servicos/', listar_servicos, name="listar_servicos"),
    path('add/servico/', add_servico, name="add_servico"),
    path('editar/servico/<int:servico_id>', editar_servico, name="editar_servico"),
    path('remove/servico/<int:servico_id>', remover_servico, name="remover_servico"),
    path('confirmar/remocao/servico/<int:servico_id>', confirmar_remocao_servico, name="confirmar_remocao_servico"),

    #detalhes do serviço
    path('detalhes/servico/<int:servico_id>', detalhes_servico, name="detalhes_servico"),
    path('listar/servicos/', listar_servicos, name="listar_servicos"),
]