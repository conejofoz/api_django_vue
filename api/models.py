from operator import mod
from tabnanny import verbose
from django.db import models

class Documento(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    expira = models.DateField()
    alerta1y = models.BooleanField(default=True)
    alerta6m = models.BooleanField(default=True)
    alerta3m = models.BooleanField(default=True)
    alerta1m = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Documento, self).save()

    class Meta:
        verbose_name_plural = "Documentos"


class Categoria(models.Model):
    descricao = models.CharField(max_length=50, null=False,blank=False, unique=True)

    def __str__(self):
        return self.descricao

    def save(self, **kwargs):
        self.descricao = self.descricao.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"
    

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "{}-{}".format(self.categoria, self.descricao)

    def save(self, **kwargs):
        self.descricao = self.descricao.upper()
        super(SubCategoria, self).save()


    class Meta:    
        verbose_name_plural = "Sub Categorias"
        unique_together = ("categoria", "descricao")


class Produto(models.Model):
    codigo = models.CharField(max_length=10, null=False, blank=False)
    descricao = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    preco = models.FloatField(default=0)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
    
    def save(self, **kwargs):
        self.descricao = self.descricao.upper()
        super(Produto, self).save()

    class Meta:
        verbose_name_plural = "Produtos"
