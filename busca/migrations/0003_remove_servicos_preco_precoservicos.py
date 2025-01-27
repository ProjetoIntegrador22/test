# Generated by Django 5.0.3 on 2024-04-01 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca', '0002_alter_provedores_options_alter_servicos_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicos',
            name='preco',
        ),
        migrations.CreateModel(
            name='PrecoServicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busca.provedores')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busca.servicos')),
            ],
            options={
                'verbose_name_plural': 'PrecoServicos',
            },
        ),
    ]
