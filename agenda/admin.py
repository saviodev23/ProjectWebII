from django.contrib import admin
from .models import Agenda, Servico, HistoricoAgendamento

admin.site.register(Agenda)
admin.site.register(Servico)
admin.site.register(HistoricoAgendamento)
# admin.site.register(ItemServico)