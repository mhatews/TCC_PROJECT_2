from django.db import models
from apps.empresas.models import Empresa

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11)
    cpf_cnpj = models.CharField(max_length=18)
    rua = models.CharField(max_length=80)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome
