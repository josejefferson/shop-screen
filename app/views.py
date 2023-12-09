from django.shortcuts import render
from .models import Produto, Anuncio

def pagina_inicial(request):
    """
    Pagina inicial

    """
    return render(request, 'index.html')

def anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'anuncios.html', {'anuncios': anuncios})

def pesquisa(request):
    return render(request, 'pesquisa.html')

def resultados_pesquisa(request):
    pesquisa = request.GET.get('q', '')
    filterNome = Produto.objects.filter(nome__icontains=pesquisa)

    return render(request, 'resultados_pesquisa.html', {'pesquisa':pesquisa, 'filterNome':filterNome})

def produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'produto.html', {'produto': produto})
