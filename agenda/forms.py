from django import forms
from .models import Servico, Agendamento
class FormAddServico(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['tipo_servico', 'nome_servico', 'preco', 'janela_tempo',]

class FormAgendamento(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['profissional', 'cliente', 'dia', 'horario', 'servico', 'status_agendamento']