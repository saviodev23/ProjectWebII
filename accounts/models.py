from django.contrib.auth.models import AbstractUser
from django.db import models
from agenda.models import Fidelidade


class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", null=True, blank=True)
    fidelidade = models.ForeignKey(Fidelidade,  on_delete=models.SET_NULL, null=True, default=None)
    desconto = models.IntegerField(default=0)

    
