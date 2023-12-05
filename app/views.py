from django.shortcuts import render
from .models import Produto, Anuncio

def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios.html', {'anuncios': anuncios})
