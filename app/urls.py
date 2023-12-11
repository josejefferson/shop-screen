from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('pesquisar', views.resultados_pesquisa, name='resultados_pesquisa'),
    path('produto/<int:id>', views.produto, name='produto'),
    path('redefinir_mais_buscados', views.redefinir_mais_buscados, name='redefinir_mais_buscados'),
    path('api/anuncios', views.anuncios_api, name='api_anuncios'),
]
