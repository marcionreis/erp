from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . models import Produto

def home(request):
    produtos = Produto.objects.all()
    template = loader.get_template('pub/home.html')
    context = {
        'prods':produtos,
        'sub_titulo': "Estoque",
    }
    return HttpResponse(template.render(context, request))