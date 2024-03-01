from .views.views_servico import add_servico, editar_servico, remover_servico, confirmar_remocao_servico, detalhes_servico, add_imagem_servico, \
    editar_imagem_servico, remover_imagem_servico, confirmar_remocao_imagem_servico, buscar_servicos
from .views.views_agenda import fazer_agendamento_pelo_profissional, listar_agendamentos_cliente, \
    listar_agendamentos, fazer_agendamento_pelo_cliente, selecione_profissional_para_agendamento, editar_agendamento, concluir_agendamento, cancelar_agendamento, buscar_agendamentos
from .views.views_fidelidade import adicionar_fidelidade, editar_fidelidade, remover_fidelidade, confirmar_remocao_fidelidade, listar_planos_fidelidade, mostrar_pontos, resgatar_fidelidade, remover_fidelidade_cliente

from django.urls import path
urlpatterns = [
    #Agendamento_pelo_profissional
    path('fazer/agendamento/', fazer_agendamento_pelo_profissional, name="fazer_agendamento_pelo_profissional"),
    path('listar/agendamentos/', listar_agendamentos, name="listar_agendamentos"),
    path('editar/agendamento/<int:agendamento_id>', editar_agendamento, name="editar_agendamento"),
    path('concluir/agendamento/<int:agendamento_id>/', concluir_agendamento, name='concluir_agendamento'),
    path('cancelar/agendamento/<int:agenda_id>', cancelar_agendamento, name="cancelar_agendamento"),
    path('buscar_agendamentos/', buscar_agendamentos, name='buscar_agendamentos'),

    #agendamento_pelo_cliente
    path('selecione/profissional/', selecione_profissional_para_agendamento,
         name="selecione_profissional_para_agendamento"),
    path('fazendo/agendamento/', fazer_agendamento_pelo_cliente, name="fazendo_agendamento_pelo_cliente"),
    path('lista/agendamentos/', listar_agendamentos_cliente, name="listar_agendamentos_cliente"),
    path('cancelar/agendamento/<int:agenda_id>', cancelar_agendamento, name="cancelar_agendamento"),

    #Crud serviço
    path('add/servico/', add_servico, name="add_servico"),
    path('editar/servico/<int:servico_id>', editar_servico, name="editar_servico"),
    path('remove/servico/<int:servico_id>', remover_servico, name="remover_servico"),
    path('confirmar/remocao/servico/<int:servico_id>', confirmar_remocao_servico, name="confirmar_remocao_servico"),
    path('buscar_servicos/', buscar_servicos, name='buscar_servicos'),

    # detalhes do serviço especifico
    path('detalhes/servico/<int:servico_id>', detalhes_servico, name="detalhes_servico"),

    #Crud imagem de servico
    path('add/imagem/servico/', add_imagem_servico, name="add_imagem_servico"),
    path('editar/imagem/servico/<int:img_servico_id>', editar_imagem_servico, name="editar_imagem_servico"),
    path('remover/imagem/servico/<int:img_servico_id>', remover_imagem_servico, name="remover_imagem_servico"),
    path('confirmar/remocao/imagem/servico/<int:img_servico_id>', confirmar_remocao_imagem_servico, name="confirmar_remocao_imagem_servico"),

    #Crud Fidelidade
    path('add/fidelidade/', adicionar_fidelidade, name="adicionar_fidelidade"),
    path('editar/fidelidade/<int:fidelidade_id>', editar_fidelidade, name="editar_fidelidade"),
    path('remove/fidelidade/<int:fidelidade_id>', remover_fidelidade, name="remover_fidelidade"),
    path('remove/fidelidade/cliente<int:user_id>', remover_fidelidade_cliente, name="remover_fidelidade_cliente"),
    path('confirmar/remocao/fidelidade/<int:fidelidade_id>', confirmar_remocao_fidelidade, name="confirmar_remocao_fidelidade"),

    path('fidelidade/', listar_planos_fidelidade, name="listar_planos_fidelidade"),
    path('fidelidade/<int:user_id>', mostrar_pontos, name="mostrar_pontos"),
    path('fidelidade/resgatar/<int:fidelidade_id>', resgatar_fidelidade, name="resgatar_fidelidade"),

]

