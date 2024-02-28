from datetime import date, time
from django.conf import settings
from django.db import models
# from django.core.exceptions import ValidationError
# from django.utils.datetime_safe import date


# def validar_dia(value):
#     today = date.today()
#     weekday = date.fromisoformat(f'{value}').weekday()
#
#     if value < today:
#         raise ValidationError('Não é possivel escolher um data atrasada.')
#     if (weekday == 5) or (weekday == 6):
#         raise ValidationError('Escolha um dia útil da semana.')

class Servico(models.Model):
    TIPO_SERVICO = (
        ('Corte', 'Corte'),
        ('Barba', 'Barba'),
        ('Sombrancelhas', 'Sombrancelhas'),
        ('Completo', 'Completo')
    )
    nome = models.CharField(max_length=50, verbose_name='Nome do Serviço')
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    tipo = models.CharField(max_length=30, choices=TIPO_SERVICO, default='Corte', verbose_name='Tipo de Serviço')
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    janela_tempo = models.TimeField(verbose_name='Duração do Serviço, ex: 00:30:00 min')

    def __str__(self):
        servico = f"{self.nome} R$:{self.preco} Duração: {self.janela_tempo} min"
        return servico

class ImagemServico(models.Model):
    servico = models.ForeignKey(Servico, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", null=True, blank=True, default=None)

    def __str__(self):
        return f'Imagem {self.pk} - {self.servico.nome}'

class Agendamento(models.Model):
    DIA_CHOICES = (
        ('Segunda', 'Segunda-Feira'),
        ('Terça', 'Terça-Feira'),
        ('Quarta', 'Quarta-Feira'),
        ('Quinta', 'Quinta-Feira'),
        ('Sexta', 'Sexta-Feira'),
    )
    STATUS_CHOICES = (
        ('AG', 'Agendado'),
        ('CA', 'Cancelado'),
        ('CO', 'Concluído')
    )
    profissional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profissional')
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    preco_servico = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço do Serviço')
    dia = models.CharField(max_length=20, verbose_name="Insira uma data para agenda", choices=DIA_CHOICES)
    horario = models.TimeField()
    status_agendamento = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='criado_por')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Agenda para {self.cliente} com {self.profissional}'

class Fidelidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome da Fidelidade')
    descricao = models.CharField(max_length=250, verbose_name='Descrição')
    desconto = models.IntegerField(default=0, verbose_name='Desconto em porcentagem')
    requisito = models.IntegerField(default=0)
    def __str__(self):
        return self.nome