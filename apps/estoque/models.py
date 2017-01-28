from django.db import models
from util.models import Cidade

# Create your models here.
class Produto(models.Model):
    codigo =  models.CharField(max_length=20, blank=False, null=False)
    nome = models.CharField(max_length=40)
    
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

class Fabricante(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=60)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
