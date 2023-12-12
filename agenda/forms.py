from django import forms
from .models import Servico
class FormAddServico(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['descricao', 'preco',]