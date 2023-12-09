from django.shortcuts import render, redirect
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
    mais_buscados = Produto.objects.all().order_by('-pesquisas')[:10]
    return render(request, 'pesquisa.html', {'mais_buscados': mais_buscados})

def resultados_pesquisa(request):
    pesquisa = request.GET.get('q', '')
    produtos = Produto.objects.filter(nome__icontains=pesquisa)

    return render(request, 'resultados_pesquisa.html', {'pesquisa':pesquisa, 'produtos':produtos})

def produto(request, id):
    produto = Produto.objects.get(id=id)
    pesquisas = produto.pesquisas + 1
    Produto.objects.filter(id=produto.id).update(pesquisas=pesquisas)

    return render(request, 'produto.html', {'produto': produto})

def redefinir_mais_buscados(request):
    Produto.objects.update(pesquisas=0)
    return redirect('/')
