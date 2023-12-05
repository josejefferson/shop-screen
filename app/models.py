from django.db import models

class Corredor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to="static/img/produtos")
    corredor = models.ForeignKey(Corredor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    imagem = models.ImageField(upload_to="static/img/anuncios")
    tempo = models.IntegerField(default=5, blank=True)
    expira = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome or "(Sem nome)"
