from django.shortcuts import render, redirect
from .models import Produto, Anuncio
from .utils import produtos_similares
import random

def index(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'index.html', {'anuncios': anuncios})

def pesquisa(request):
    todos_produtos = Produto.objects.all().order_by('-pesquisas')
    mais_buscados = todos_produtos[:10]
    sugestoes = list(todos_produtos)
    random.shuffle(sugestoes)
    return render(request, 'pesquisa.html', {
        'mais_buscados': mais_buscados,
        'sugestoes': sugestoes[:12]
    })

def resultados_pesquisa(request):
    pesquisa = request.GET.get('q', '')
    produtos = Produto.objects.filter(nome__icontains=pesquisa.strip())

    return render(request, 'resultados_pesquisa.html', {'pesquisa':pesquisa, 'produtos':produtos})

def produto(request, id):
    produto = Produto.objects.get(id=id)
    pesquisas = produto.pesquisas + 1
    Produto.objects.filter(id=produto.id).update(pesquisas=pesquisas)
    similares = produtos_similares(produto)
    mais_buscados = Produto.objects.all().order_by('-pesquisas')[:10]

    return render(request, 'produto.html', {
        'produto': produto,
        'similares': similares,
        'mais_buscados': mais_buscados,
    })

def redefinir_mais_buscados(request):
    Produto.objects.update(pesquisas=0)
    return redirect('/')
