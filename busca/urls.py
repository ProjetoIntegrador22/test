from django.urls import path
from busca import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('pesquisa', views.pesquisa, name='pesquisa')
]