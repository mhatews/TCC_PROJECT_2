# Generated by Django 4.2.1 on 2023-06-11 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('produtos', '0004_rename_nome_produto_produto_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
    ]
