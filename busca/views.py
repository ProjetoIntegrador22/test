from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'busca/index.html')

def sobre(request):
    return render(request, 'busca/sobre.html')

def contato(request):
    return render(request, 'busca/contato.html')

def pesquisa(request):
    return render(request, 'busca/pesquisa.html')



