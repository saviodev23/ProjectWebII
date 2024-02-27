from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", null=True, blank=True)
    desconto = models.IntegerField(default=0)
    agendamentos_concluidos = models.IntegerField(default=0)
    cupon = models.IntegerField(default=0)
