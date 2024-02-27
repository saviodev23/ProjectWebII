from django import forms
from horario.models import Disponibilidade, Parametro

class AddDisponibilidade(forms.ModelForm):
    widgets = {
        'profissional': forms.Select(attrs={'class': 'form-control'}),
        'dia': forms.Select(attrs={'class': 'form-control'}),
        'horario_inicio': forms.TimeInput(attrs={'class': 'form-control'}),
        'horario_fim': forms.TimeInput(attrs={'class': 'form-control'}),
    }

    class Meta:
        model = Disponibilidade
        fields = ['profissional', 'dia', 'horario_inicio', 'horario_fim',]



class AddParametro(forms.ModelForm):

    class Meta:
        model = Parametro
        fields = ['nome', 'valor', 'criado_por']
