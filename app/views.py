from django.core import serializers
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Produto, Anuncio
from .utils import produtos_similares
from fuzzywuzzy import process
from unidecode import unidecode
import json
import random
from datetime import datetime

def index(request):
    """Rota principal dos anúncios"""
    nao_expirou = Q(expira__gte=datetime.now()) | Q(expira__isnull=True)
    anuncios = Anuncio.objects.filter(nao_expirou)
    return render(request, 'index.html', {'anuncios': anuncios})

def pesquisa(request):
    """Página de pesquisa"""
    todos_produtos = Produto.objects.all().order_by('-pesquisas')
    mais_buscados = todos_produtos[:10]
    sugestoes = list(todos_produtos)
    random.shuffle(sugestoes)
    return render(request, 'pesquisa.html', {
        'mais_buscados': mais_buscados,
        'sugestoes': sugestoes[:12]
    })

def resultados_pesquisa(request):
    """Página de resultados da pesquisa"""
    pesquisa = unidecode(request.GET.get('q', '').lower().strip())
    todos_produtos = Produto.objects.all()
    nomes = list(map(lambda produto: unidecode(produto.nome.lower().strip()), todos_produtos))
    resultados = process.extract(pesquisa, nomes, limit=99999)

    produtos = []
    for resultado, proximidade in resultados:
        index = nomes.index(resultado)
        produto = todos_produtos[index]
        if proximidade >= 50:
            produtos.append(produto)

    return render(request, 'resultados_pesquisa.html', {'pesquisa':pesquisa, 'produtos':produtos})

def produto(request, id):
    """Página de visualização do produto"""
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

def anuncios_api(request):
    nao_expirou = Q(expira__gte=datetime.now()) | Q(expira__isnull=True)
    resultado = Anuncio.objects.filter(nao_expirou)
    json_str = serializers.serialize('json', resultado)
    json_resultado = json.loads(json_str)
    return JsonResponse(json_resultado, safe=False)

def redefinir_mais_buscados(request):
    """Rota para redefinir os produtos mais buscados"""
    Produto.objects.update(pesquisas=0)
    return redirect('/')
