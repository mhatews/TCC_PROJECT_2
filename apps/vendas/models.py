from django.db import models
from django.db.models import Sum
from apps.produtos.models import Produto
from apps.clientes.models import Cliente
from apps.empresas.models import Empresa
from apps.core.models import Financeiro

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, through='ItemVenda')
    data = models.DateField()
    data_recebimento = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calcular_valor_total(self):
        total = sum(item.calcular_subtotal() for item in self.itemvenda_set.all())
        self.valor_total = total
        self.save()

    def save(self, *args, **kwargs):
        self.calcular_valor_total()
        super(Venda, self).save(*args, **kwargs)

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, null=True, blank=True )
    quantidade = models.IntegerField()

    def calcular_subtotal(self):
        return self.quantidade * self.produto.valor_unitario