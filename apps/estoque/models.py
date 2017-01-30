from django.db import models
from utils.models import Cidade


# Create your models here.
class Fabricante(models.Model):
    nome = models.CharField(max_length=64)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=256)
    cidade = models.ForeignKey(Cidade)
    
    class Meta:
        # https://docs.djangoproject.com/en/1.10/ref/models/options/#unique-together
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"
    
    def __str__(self):
        return "{n}".format(n=self.nome)


class Marca(models.Model):
    nome = models.CharField(max_length=64)
    fabricante = models.ForeignKey(Fabricante)
    
    class Meta:
        unique_together = ('nome', 'fabricante')
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
    
    def __str__(self):
        return "{n}".format(n=self.nome)
        
class Produto(models.Model):
    codigo = models.CharField(max_length=16, unique=True)
    nome = models.CharField(max_length=64)
    marca = models.foreignKey(Marca)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"    
    
    def __str__(self):
        return "{n}".format(n=self.nome)