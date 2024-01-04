
from datetime import time
from django.contrib.auth.models import User
from django.db import models

# class Usuario()

class Disponibilidade(models.Model):
    DIA_CHOICES = (
        ('Segunda', 'Segunda-Feira'),
        ('Terça', 'Terça-Feira'),
        ('Quarta', 'Quarta-Feira'),
        ('Quinta', 'Quinta-Feira'),
        ('Sexta', 'Sexta-Feira'),
    )
    profissional = models.ForeignKey(User, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20, choices=DIA_CHOICES)
    horario_inicio = models.TimeField(default=time())
    horario_fim = models.TimeField(default=time())

class Parametro(models.Model):
    PRECO_CHOICES = (
        ('1', '10.00'),
        ('2', '15.00'),
        ('3', '20.00'),
        ('4', '30.00'),
    )
    nome = models.CharField(max_length=30)
    preco = models.CharField(max_length=20, choices=PRECO_CHOICES)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateField()