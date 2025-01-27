# Generated by Django 5.0.3 on 2024-04-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca', '0004_precoservicos_ultima_atualizacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='precoservicos',
            name='provedor',
        ),
        migrations.RemoveField(
            model_name='precoservicos',
            name='servico',
        ),
        migrations.AddField(
            model_name='precoservicos',
            name='provedor',
            field=models.ManyToManyField(to='busca.provedores'),
        ),
        migrations.AddField(
            model_name='precoservicos',
            name='servico',
            field=models.ManyToManyField(to='busca.servicos'),
        ),
    ]
