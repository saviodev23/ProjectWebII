from .views.views_servico import add_servico, editar_servico, remover_servico, confirmar_remocao_servico, detalhes_servico
from .views.views_agenda import fazer_agendamento_pelo_profissional, etapa_de_agendamento, listar_agendamentos_cliente, listar_agendamentos, editar_agendamento,concluir_agendamento
from .views.views_fidelidade import adicionar_fidelidade, editar_fidelidade, remover_fidelidade, confirmar_remocao_fidelidade
from django.urls import path
from ProjectWebII.utils import mostrar_pontos, resgatar_fidelidade, remover_fidelidade_cliente

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
    path('Fidelidade/resgatar/<int:fidelidade_id>', resgatar_fidelidade, name="resgatar_fidelidade"),
    path('Fidelidade/add/', adicionar_fidelidade, name="adicionar_fidelidade"),
    path('editar/fidelidade/<int:fidelidade_id>', editar_fidelidade, name="editar_fidelidade"),
    path('remove/fidelidade/<int:fidelidade_id>', remover_fidelidade, name="remover_fidelidade"),
    path('remove/fidelidade/cliente<int:user_id>', remover_fidelidade_cliente, name="remover_fidelidade_cliente"),
    path('confirmar/remocao/fidelidade/<int:fidelidade_id>', confirmar_remocao_fidelidade, name="confirmar_remocao_fidelidade"),

    


    #detalhes do serviço especifico
    path('detalhes/servico/<int:servico_id>', detalhes_servico, name="detalhes_servico"),
]