from django.contrib.auth.models import AbstractUser
from django.db import models



class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    imagem = models.ImageField(upload_to="images/%Y/%m/%d/", null=True, blank=True)

