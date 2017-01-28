from django.contrib import admin
from . models import Estado, Regiao, Cidade
# Register your models here.


class EstadoInline(admin.TabularInline):
    model = Estado
    extra = 0


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 0


class AdminEstado(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'regiao']
    list_filter = ['regiao']
    inlines = [CidadeInline]


class AdminCidade(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'ddd']
    list_filter = ['estado']


class AdminRegiao(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    list_filter = ['nome']
    inlines = [EstadoInline]


admin.site.register(Regiao, AdminRegiao)
admin.site.register(Estado, AdminEstado)
admin.site.register(Cidade, AdminCidade)
