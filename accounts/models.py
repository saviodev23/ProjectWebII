from django.contrib.auth.models import AbstractUser
from django.db import models
from agenda.models import Fidelidade

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", null=True, blank=True)
    desconto = models.IntegerField(default=0)
    fidelidade = models.ForeignKey(Fidelidade,  on_delete=models.SET_NULL, null=True, default=None, blank=True)