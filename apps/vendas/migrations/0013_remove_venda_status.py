# Generated by Django 4.2.1 on 2023-09-29 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0012_venda_data_recebimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='status',
        ),
    ]
