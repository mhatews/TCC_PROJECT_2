# Generated by Django 4.2.1 on 2023-06-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0007_remove_itemvenda_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
