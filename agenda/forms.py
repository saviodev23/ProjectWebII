from django import forms
from .models import Servico, Agendamento
from django.forms import ModelForm

class FormAddServico(forms.ModelForm):
    widgets = {
        'imagem': forms.FileInput(attrs={'id': 'upload', 'accept': "image/*", 'required': True})
    }

    class Meta:
        model = Servico
        fields = "__all__"

class FormAgendamento(forms.ModelForm):
    dia = forms.DateField(label='Dia de Agendamento')
    horario = forms.TimeField(label='Horário de Agendamento')
    class Meta:
        model = Agendamento
        fields = ['profissional', 'cliente', 'dia', 'horario', 'servico','preco_servico','criado_por', 'criado_em']

class FormEditarAgendamento(ModelForm):
    class Meta:
        model = Agendamento

        fields = ['status_agendamento']

