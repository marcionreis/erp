from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . models import Produto, Categoria

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


def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    produtos = Produto.objects.filter(categoria=categoria)
    template = loader.get_template('pub/categoria.html')
    context = {
        'categoria': categoria,
        'produtos': produtos,
        'sub_titulo': SUB_TITULO,
    }
    
    return HttpResponse(template.render(context, request))