from django.db import models
from apps.empresas.models import Empresa


class Servico(models.Model):
    nome = models.CharField(max_length=50)
    valor_uni = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
