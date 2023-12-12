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

# class ItemServico(models.Model):
#     TIPO_CHOICES = [
#         ('Corte', 'Corte de Cabelo'),
#         ('Coloracao', 'Coloração de Cabelo'),
#         ('Alisamento', 'Alisamento'),
#         ('Manicure', 'Manicure'),
#         ('Pedicure', 'Pedicure'),
#         ('Sombrancelhas', 'Sombrancelhas'),
#     ]
#     nome = models.CharField(max_length=50, choices=TIPO_CHOICES)
#     preco = models.DecimalField(max_digits=8, decimal_places=2)
#
#     def __str__(self):
#         return self.nome
class Servico(models.Model):
    TIPO_CHOICES = [
        ('Unhas', 'Unhas'),
        ('Cosmedicos', 'Cosmédicos'),
        ('Cabelereiro', 'Cabelereiro'),
    ]
    NOME_CHOICES = [
        ('Corte', 'Corte de Cabelo'),
        ('Coloracao', 'Coloração de Cabelo'),
        ('Alisamento', 'Alisamento'),
        ('Manicure', 'Manicure'),
        ('Pedicure', 'Pedicure'),
        ('Sombrancelhas', 'Sombrancelhas'),
    ]
    tipo_servico = models.CharField(max_length=50, choices=TIPO_CHOICES)
    nome_servico = models.CharField(max_length=50, choices=NOME_CHOICES)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        servico = f"Nome Serviço: {self.nome_servico} Tipo Serviço:{self.tipo_servico}"
        return servico

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
    # servico = models.ManyToManyField(Servico, related_name='agendas')
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])
    horario = models.CharField(max_length=1, choices=HORARIOS)
    status_agendamento = models.BooleanField()

    def __str__(self):
        return f'Agenda para {self.cliente.username} com {self.profissional.username}'

class HistoricoAgendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente.username} - {self.data_agendamento}"