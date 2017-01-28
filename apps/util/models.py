from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome da Região")
    sigla = models.CharField(max_length=2, unique=True, verbose_name = "Sigla", help_text="Sigla do estado")

    def __str__(self):
        return "{sg} - {nm}".format(sg=self.sigla, nm=self.nome)

    class Meta:
        verbose_name = "Região"
        verbose_name_plural = "Regiões"


class Estado(models.Model):
    nome = models.CharField(max_length=20)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

    def __str__(self):
        return "{sg} - {nm}".format(sg=self.sigla, nm=self.nome)
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Cidade(models.Model):
    nome = models.CharField(max_length=32)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    ddd = models.CharField(max_length=3)
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"