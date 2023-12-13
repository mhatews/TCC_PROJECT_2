# Generated by Django 4.2.1 on 2023-12-12 09:42

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0025_alter_venda_valor_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]