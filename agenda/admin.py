from django.contrib import admin
from .models import Agendamento, Servico, Fidelidade, ImagemServico

admin.site.register(Agendamento)
admin.site.register(Servico)
admin.site.register(Fidelidade)
admin.site.register(ImagemServico)