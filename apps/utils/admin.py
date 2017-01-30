from django.contrib import admin
from . models import Regiao, Estado, Cidade

# INLINES
class EstadoInline(admin.TabularInline):
    model = Estado
    extra = 0


class CidadeInline(admin.StackedInline):
    model = Cidade
    extra = 0

# MODEL ADMIN
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'regiao')
    list_filter = ('regiao',)
    inlines = [
        CidadeInline,
        ]

class RegiaoAdmin(admin.ModelAdmin):
    inlines = [
        EstadoInline,
    ]
    
admin.site.register(Regiao, RegiaoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade)