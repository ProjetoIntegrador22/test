# Generated by Django 5.0.3 on 2024-04-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca', '0005_remove_precoservicos_provedor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaTeste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=20)),
                ('cnpj', models.DecimalField(decimal_places=0, max_digits=14)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('servico', models.CharField(max_length=100)),
            ],
        ),
    ]
