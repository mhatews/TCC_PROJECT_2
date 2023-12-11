# Generated by Django 4.2.1 on 2023-06-13 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_alter_empresa_nome'),
        ('vendas', '0003_remove_venda_produto_remove_venda_quantidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvenda',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venda',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
    ]
