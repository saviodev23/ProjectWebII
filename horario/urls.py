from.views import add_disponibilidade, remover_disponibilidade, editar_disponibilidade, confirmar_remocao_disponibilidade
from django.urls import path
urlpatterns = [
    # crud_disponibilidade
    path('add/disponibilidade/', add_disponibilidade, name="add_disponibilidade"),
    path('editar/disponibilidade/<int:dispo_id>', editar_disponibilidade, name="editar_disponibilidade"),
    path('remover/disponibilidade/<int:dispo_id>', remover_disponibilidade, name="remover_disponibilidade"),
    path('confirmar/remocao/disponibilidade/<int:dispo_id>', confirmar_remocao_disponibilidade, name="confirmar_remocao_disponibilidade"),

]