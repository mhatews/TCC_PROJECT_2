from django.db import models
from apps.empresas.models import Empresa


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
