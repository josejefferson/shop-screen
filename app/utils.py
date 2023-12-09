from difflib import SequenceMatcher
from .models import Produto

def similarity(a, b):
    """
    Retorna o grau de similaridade entre 2 strings
    """
    return SequenceMatcher(None, a, b).ratio()

def produtos_similares(produto):
    produtos = Produto.objects.exclude(id=produto.id)
    produtos_ordenados = sorted(produtos, key=lambda p: similarity(produto.nome, p.nome))
    produtos_ordenados.reverse()
    similares = produtos_ordenados[:8]
    return similares
