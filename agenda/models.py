from datetime import date, time
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Escolha um dia útil da semana.')

class Servico(models.Model):
    nome_servico = models.CharField(max_length=50, verbose_name='Nome do Serviço')
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    janela_tempo = models.TimeField(default=time(), verbose_name='Duração do Serviço')
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", null=True)

    def __str__(self):
        servico = f"Nome Serviço: {self.nome_servico} Preço Serviço:{self.preco}"
        return servico

class Agendamento(models.Model):
    STATUS_CHOICES = (
        ('AG', 'Agendado'),
        ('CA', 'Cancelado'),
        ('CO', 'Concluído')
    )
    profissional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profissional')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente', blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])
    horario = models.TimeField()
    status_agendamento = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='criado_por')
    criado_em = models.DateTimeField()

    def __str__(self):
        return f'Agenda para {self.cliente.username} com {self.profissional.username}'

class Fidelidade(models.Model):
    STATUS_CHOICES = (
        ('CA', 'Cancelado'),
        ('CO', 'Concluido'),
    )
    agenda = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.status