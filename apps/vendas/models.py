from django.db import models
from decimal import Decimal
from django.db.models import Sum
from apps.produtos.models import Produto
from apps.clientes.models import Cliente
from apps.empresas.models import Empresa
from apps.core.models import Financeiro

        
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data = models.DateField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT, default=1)
    data_recebimento = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def calcular_valor_total(self):
       
        total = 0
        for item in self.itemvenda_set.all():
            total += item.get_valor_total()
        self.valor_total = total
        self.save()

        '''
       # Obtém a soma dos subtotais dos itens de venda associados a esta venda
        valor_total = self.itemvenda_set.aggregate(Sum('sub_total_item'))['sub_total_item__sum']

        

        # Atualiza o campo 'valor_total' da venda
        self.valor_total = valor_total if valor_total is not None else Decimal('0.00')
        self.save()'''

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Venda, self).save(*args, **kwargs)
            for item in self.itemvenda_set.all():
                item.save()
            self.calcular_valor_total()
        else:
            super(Venda, self).save(*args, **kwargs)


class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey('Venda', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_unitario_na_venda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sub_total_item =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def get_valor_total(self):
        return self.quantidade * self.valor_unitario_na_venda
    
    
    def save(self, *args, **kwargs):

        
        # Armazenar o valor unitário do produto no momento da venda
        self.valor_unitario_na_venda = self.produto.valor_unitario

        self.sub_total_item = self.quantidade * self.valor_unitario_na_venda
        super(ItemVenda, self).save(*args, **kwargs)


class Status(models.Model):
     nome = models.CharField(max_length=100)

     def __str__(self):
        return self.nome
