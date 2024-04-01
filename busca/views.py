from django.shortcuts import render
from busca.models import ListaTeste


# Create your views here.

def index(request):
    return render(request, 'busca/index.html')

def sobre(request):
    return render(request, 'busca/sobre.html')

def contato(request):
    return render(request, 'busca/contato.html')

def pesquisa(request):
    items = ListaTeste.objects.all()
    lista_provedores = {'provedores': items}
    return render(request, 'busca/pesquisa.html', lista_provedores)



