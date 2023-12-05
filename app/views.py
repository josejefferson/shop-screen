from django.shortcuts import render
from .models import Produto, Anuncio

def pagina_inicial(request):
    return render(request, 'index.html')

def anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios.html', {'anuncios': anuncios})

def pesquisa(request):
    return render(request, 'pesquisa.html')

def resultados_pesquisa(request):
    pesquisa = request.GET['q']
    return render(request, 'resultados_pesquisa.html', {'pesquisa':pesquisa})

def produto(request, id):
    return render(request, 'produto.html')
