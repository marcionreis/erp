from django.db import models

class Regiao(models.Model):
    nome = models.CharField(max_length=32, unique=True, verbose_name="Nome")
    sigla = models.CharField(max_length=2, unique=True, verbose_name="Sigla")
    
    class Meta:
        verbose_name = "Região"
        verbose_name_plural = "Regiões"
    
    def __str__(self):
        return "{n}".format(n=self.nome, s=self.sigla)


class Estado(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.ForeignKey(Regiao, verbose_name="Região")
    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"    
    
    def __str__(self):
        return "{n}".format(n=self.nome)


class Cidade(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    estado = models.ForeignKey(Estado)
    ddd = models.CharField(max_length=2, verbose_name="DDD", help_text="Discagem Direta à Distância")
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
    
    def __str__(self):
        return "{n}".format(n=self.nome)
