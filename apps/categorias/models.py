from django.db import models
from apps.empresas.models import Empresa
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
