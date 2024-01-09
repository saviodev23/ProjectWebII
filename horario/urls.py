from.views import add_disponibilidade, remover_disponibilidade, editar_disponibilidade, confirmar_remocao_disponibilidade, add_parametro, editar_parametro, remover_parametro, confirmar_remocao_parametro
from django.urls import path
urlpatterns = [
    # crud_disponibilidade
    path('add/disponibilidade/', add_disponibilidade, name="add_disponibilidade"),
    path('editar/disponibilidade/<int:dispo_id>', editar_disponibilidade, name="editar_disponibilidade"),
    path('remover/disponibilidade/<int:dispo_id>', remover_disponibilidade, name="remover_disponibilidade"),
    path('confirmar/remocao/disponibilidade/<int:dispo_id>', confirmar_remocao_disponibilidade, name="confirmar_remocao_disponibilidade"),
    # crud_parametro
    path('add/parametro/', add_parametro, name="add_parametro"),
    path('editar/parametro/<int:parametro_id>', editar_parametro, name="editar_parametro"),
    path('remover/parametro/<int:parametro_id>', remover_parametro, name="remover_parametro"),
    path('confirmar/remocao/parametro/<int:parametro_id>', confirmar_remocao_parametro, name="confirmar_remocao_parametro"),

]