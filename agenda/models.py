from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

class Agenda(models.Model):
    profissional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profissional')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente')
    agendado = models.BooleanField(blank=True, null=True)

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.DateTimeField()
