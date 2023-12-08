import datetime
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Escolha um dia útil da semana.')

class Servico(models.Model):
    DESCRICAO_CHOICES = [
        ('corte', 'Corte de Cabelo'),
        ('coloracao', 'Coloração de Cabelo'),
        ('alisamento', 'Alisamento'),
        ('manicure', 'Manicure'),
    ]
    descricao = models.CharField(max_length=50, choices=DESCRICAO_CHOICES)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.descricao

class Agenda(models.Model):
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    profissional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profissional')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente')
    servico = models.ManyToManyField(Servico, related_name='agendas')
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])
    horario = models.CharField(max_length=1, choices=HORARIOS)
    status = models.BooleanField()

    def __str__(self):
        return f'Agenda para {self.cliente.username} com {self.profissional.username}'

class HistoricoAgenda(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)