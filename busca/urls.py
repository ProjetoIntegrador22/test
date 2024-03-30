from django.urls import path
from busca.views import index

urlpatterns = [
    path('', index, name='index')
]