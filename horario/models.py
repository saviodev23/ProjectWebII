from django.conf import settings
from django.db import models
from datetime import time
class Disponibilidade(models.Model):
    DIA_CHOICES = (
        ('Segunda', 'Segunda-Feira'),
        ('Terça', 'Terça-Feira'),
        ('Quarta', 'Quarta-Feira'),
        ('Quinta', 'Quinta-Feira'),
        ('Sexta', 'Sexta-Feira'),
    )
    profissional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20, choices=DIA_CHOICES)
    horario_inicio = models.TimeField(default=time())
    horario_fim = models.TimeField(default=time())

class Horarios(models.Model):
    disponibilidade = models.ForeignKey(Disponibilidade, on_delete=models.CASCADE)
    horario_disponivel = models.TimeField()

class Parametro(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.IntegerField(default=30)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)