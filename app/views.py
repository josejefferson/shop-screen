from django.shortcuts import render
from .models import Produto


def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})
