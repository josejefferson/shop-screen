from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('anuncios', views.anuncios, name='anuncios'),
]
