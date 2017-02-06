from django.db import models
from django.urls import reverse
#from django.core.urlresolvers import reverse
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
        # https://docs.djangoproject.com/en/1.10/ref/models/options/
        unique_together = ('nome', 'fabricante')
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    
    
    def __str__(self):
        return "{n}".format(n=self.nome)


class Categoria(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return "{n}".format(n=self.nome)


class Produto(models.Model):
    codigo = models.CharField(max_length=16, unique=True)
    nome = models.CharField(max_length=64)
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria,)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"    
    
    def __str__(self):
        return "{n}".format(n=self.nome)

    def get_absolute_url(self):
        return reverse('estoque:produto', kwargs={'id':self.id})
        #"/estoque/produto/{cod}".format(cod=self.codigo)

    
class Lote(models.Model):
    codigo = models.CharField(max_length=16, unique=True)
    produto = models.ForeignKey(Produto)
    data_validade = models.DateField()
    
    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"
    
    def __str__(self):
        return "[{c}]p".format(p=self.produto, c=self.codigo)

class Prateleira(models.Model):
    codigo = models.CharField(max_length=16)
    categoria = models.ForeignKey(Categoria)
    
    class Meta:
        verbose_name = "Prateleira"
        verbose_name_plural = "Prateleiras"
    
    def __str__(self):
        return "[{c}]cat".format(cat=self.categoria, c=self.codigo)
    
class Estoque(models.Model):
    lote = models.ForeignKey(Lote)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    prateleira = models.ForeignKey(Prateleira)
    
    class Meta:
        unique_together = ('lote', 'prateleira')
        verbose_name = "Estoque"
        verbose_name_plural = "Estoque de Produtos"
    
    def __str__(self):
        return "[{c}]:{l}".format(l=self.lote, c=self.codigo)