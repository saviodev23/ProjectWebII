from django import forms
from horario.models import Disponibilidade


class AddDisponibilidade(forms.ModelForm):
    class Meta:
        model = Disponibilidade
        fields = ['profissional', 'dia', 'horario_inicio', 'horario_fim',]

        # widgets = {
        #     'horario_inicio': forms.TimeInput(attrs={'class': 'form-control'}),
        #     'horario_fim': forms.TimeInput(attrs={'class': 'form-control'}),
        # }