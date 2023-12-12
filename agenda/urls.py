from .views import fazer_agendamento, add_servico, editar_servico, remover_servico, confirmar_remocao_servico
from django.urls import path

urlpatterns = [
    path('ver_agenda/', fazer_agendamento, name="ver_agenda"),
    #Crud serviço
    path('add/servico/', add_servico, name="add_servico"),
    path('editar/servico/<int:servico_id>', editar_servico, name="editar_servico"),
    path('remove/servico/<int:servico_id>', remover_servico, name="remover_servico"),
    path('confirmar/remocao/servico/<int:servico_id>', confirmar_remocao_servico, name="confirmar_remocao_servico"),

]