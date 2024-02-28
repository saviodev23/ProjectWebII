from django import forms
from .models import Servico, Agendamento, ImagemServico, Fidelidade


class FormAddServico(forms.ModelForm):

    class Meta:
        model = Servico
        fields = "__all__"

class ImagemServicoForm(forms.ModelForm):

    widgets = {
        'imagem': forms.FileInput(attrs={'id': 'upload', 'accept': "image/*", 'required': True})
    }
    class Meta:
        model = ImagemServico
        fields = ['servico', 'imagem']
class FormAgendamentoCliente(forms.ModelForm):
    # dia = forms.DateField(label='Dia de Agendamento')
    # horario = forms.TimeField(label='Horário de Agendamento')
    widgets = {
        'dia': forms.Select(attrs={'class': 'form-select'}),
        'horario': forms.Select(attrs={'class': 'form-select'}),
        'servico': forms.Select(attrs={'class': 'form-select'}),
    }
    class Meta:
        model = Agendamento
        fields = ['dia', 'horario', 'servico']

class FormAgendamentoProfissional(forms.ModelForm):
    # dia = forms.DateField(label='Dia de Agendamento')
    # horario = forms.TimeField(label='Horário de Agendamento')
    # widgets = {
    #     'dias': forms.Select(attrs={'class': 'form-control'}),
    #     'horarios': forms.Select(attrs={'class': 'form-control'}),
    # }
    class Meta:
        model = Agendamento
        fields = ['dia', 'horario', 'servico', 'criado_por', 'cliente', 'profissional']

class FormEditarAgendamento(forms.ModelForm):
    class Meta:
        model = Agendamento

        fields = ['status_agendamento']


class FormFidelidade(forms.ModelForm):
    class Meta:
        model = Fidelidade
        fields = ['nome', 'descricao', 'desconto', 'requisito']
        labels = {
            'requisito': 'Quantidade de cortes para receber o desconto',
        }