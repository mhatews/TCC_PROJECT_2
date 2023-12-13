from django.db import models
from decimal import Decimal
from django.db.models import Sum
from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.empresas.models import Empresa
from apps.core.models import Financeiro

        
class Ordem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data = models.DateField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT, default=1)
    data_recebimento = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def calcular_valor_total(self, *args, **kwargs):

        
       # Obtém a soma dos subtotais dos itens de venda associados a esta venda
        valor_total = self.itemordem_set.aggregate(Sum('sub_total_item'))['sub_total_item__sum']

        

        # Atualiza o campo 'valor_total' da venda
        self.valor_total = valor_total if valor_total is not None else Decimal('0.00')
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Ordem, self).save(*args, **kwargs)
            for item in self.itemordem_set.all():
                item.save()
            self.calcular_valor_total()
        else:
            super(Ordem, self).save(*args, **kwargs)


class ItemOrdem(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    ordem = models.ForeignKey('Ordem', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_unitario_na_ordem = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sub_total_item =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):

        
        # Armazenar o valor unitário do produto no momento da venda
        self.valor_unitario_na_ordem = self.servico.valor_uni

        self.sub_total_item = self.quantidade * self.valor_unitario_na_ordem
        super(ItemOrdem, self).save(*args, **kwargs)

class Status(models.Model):
     nome = models.CharField(max_length=100)

     def __str__(self):
        return self.nome

