# Generated by Django 4.2.1 on 2023-06-20 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('vendas', '0009_remove_venda_valor_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.financeiro'),
            preserve_default=False,
        ),
    ]
