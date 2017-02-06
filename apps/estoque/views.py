from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . models import Produto

SUB_TITULO = "Estoque"

def home(request):
    produtos = Produto.objects.all()
    template = loader.get_template('pub/home.html')
    context = {
        'prods': produtos,
        'sub_titulo': SUB_TITULO,
    }
    
    return HttpResponse(template.render(context, request))

def produto(request, id):
	produto = Produto.objects.get(id=id)
	template = loader.get_template("pub/produto.html")

	context = {
        'produto': produto,
        'sub_titulo': SUB_TITULO,
    }

	return HttpResponse(template.render(context, request))