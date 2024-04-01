from django.contrib import admin
from busca import models

# Register your models here.

class VisualPreco(admin.ModelAdmin):
    list_display = ('preco', 'ultima_atualizacao')

class VisualProvedores(admin.ModelAdmin):
    list_display = ('id', 'apelido', 'cnpj')
    list_display_links = ('id', 'apelido')



admin.site.register(models.Provedores, VisualProvedores)
admin.site.register(models.Disponibilidade)
admin.site.register(models.Servicos)
admin.site.register(models.PrecoServicos, VisualPreco)
admin.site.register(models.ListaTeste, VisualProvedores)
