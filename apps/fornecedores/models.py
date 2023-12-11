from django.db import models
from apps.empresas.models import Empresa


class Fornecedor(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=80)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
