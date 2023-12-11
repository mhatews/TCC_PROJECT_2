from django.db import models
from apps.empresas.models import Empresa
from apps.categorias.models import Categoria




class Produto(models.Model):
    nome = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)



    def __str__(self):
        return self.nome