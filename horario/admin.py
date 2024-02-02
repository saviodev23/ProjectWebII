from django.contrib import admin

from .models import Disponibilidade, Parametro, Horarios

admin.site.register(Disponibilidade)
admin.site.register(Parametro)
admin.site.register(Horarios)
