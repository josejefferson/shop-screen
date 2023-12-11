from difflib import SequenceMatcher
from .models import Produto

def similarity(a: str, b: str) -> float:
    """
    Retorna o grau de similaridade entre 2 strings

    Parameters:
        a (str): Primeira string
        b (str): Segunda string

    Returns:
        ratio (float): Similaridade entre as strings, entre 0 e 1
    """
    return SequenceMatcher(None, a, b).ratio()

def produtos_similares(produto):
    """
    Retorna uma lista com 8 produtos similares ao produto passado pelo parâmetro

    Parameters:
        produto: Produto com nome para comparar

    Returns:
        similares: Lista com, no máximo, 8 produtos com nomes similares
    """
    produtos = Produto.objects.exclude(id=produto.id)
    produtos_ordenados = sorted(produtos, key=lambda p: similarity(produto.nome, p.nome))
    produtos_ordenados.reverse()
    similares = produtos_ordenados[:8]
    return similares
