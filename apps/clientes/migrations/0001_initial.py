# Generated by Django 4.2.1 on 2023-06-07 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=11)),
                ('cpf_cnpj', models.CharField(max_length=18)),
                ('rua', models.CharField(max_length=80)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
    ]
