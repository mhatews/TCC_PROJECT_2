from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Venda


@receiver(post_save, sender=Venda)
def calcular_valor_total(sender, instance, created, **kwargs):
    if created:
        instance.calcular_valor_total()
        instance.save()