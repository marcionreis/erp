from django.shortcuts import render

from . models import Cidade
# Create your views here.

def findAllCidades():
    return Cidade.nome