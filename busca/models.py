from django.db import models
from datetime import datetime

# Create your models here.

class Provedores(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=20)
    cnpj = models.DecimalField(max_digits=14, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Provedores'

    def __str__(self):
        return self.apelido

class Servicos(models.Model):
    provedor = models.ManyToManyField(Provedores)
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.nome

class Disponibilidade(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    data = models.DateField()
    local = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.servico
    
class PrecoServicos(models.Model):
    servico = models.ManyToManyField(Servicos)
    provedor = models.ManyToManyField(Provedores)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ultima_atualizacao = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = 'PrecoServicos'

    
class ListaTeste(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=20)
    cnpj = models.DecimalField(max_digits=14, decimal_places=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    servico = models.CharField(max_length=100)

    def __str__(self):
        return self.apelido
    
    class Meta:
        verbose_name_plural = 'Testes'