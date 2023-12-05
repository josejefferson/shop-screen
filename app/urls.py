from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('anuncios', views.anuncios, name='anuncios'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('pesquisar', views.resultados_pesquisa, name='resultados_pesquisa'),
    path('produto/<int:id>', views.produto, name='produto'),
]
