from django.contrib import admin
from . models import Fabricante, Marca, Produto, Categoria, Lote, Prateleira, Estoque

# INLINES
class MarcaInline(admin.TabularInline):
    model = Marca
    extra = 0

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 0

# MODELADMIN
class FabricanteAdmin(admin.ModelAdmin):
    inlines = [
        MarcaInline,
    ]

class MarcaAdmin(admin.ModelAdmin):
    inlines = [
        ProdutoInline,
    ]
    

class ProdutoAdmin(admin.ModelAdmin):
    list_filter = ('marca', 'marca__fabricante', 'categoria')
    list_display = ('nome', 'marca', 'codigo', 'categoria')
    search_fields = ['codigo', 'nome']


# REGISTERs
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Lote)
admin.site.register(Prateleira)
admin.site.register(Estoque)
