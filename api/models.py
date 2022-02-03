from operator import mod, truediv
from tabnanny import verbose
from tkinter.tix import Tree
from django.db import models
#from importlib_metadata import email


class ModeloEdit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
    categoria = models.ForeignKey(Categoria, related_name='subcategorias', on_delete=models.CASCADE)
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


class Fornecedor(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False,unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nome

    def save(self, **kwargs):
        self.nome = self.nome.upper()
        super(Fornecedor, self).save()

    class Meta:
        verbose_name_plural = 'Fornecedores'
    

class Compras(ModeloEdit):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data = models.DateField(null=False, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Compras"
    

class ComprasDetalhe(ModeloEdit):
    compra = models.ForeignKey(Compras, related_name='detalhe', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(default=0)
    preco = models.FloatField(default=0)
    desconto = models.FloatField(default=0)

    @property
    def subtotal(self):
        return self.quantidade * self.preco

    @property
    def total(self):
        return self.subtotal - self.desconto

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.compra, self.produto)

    class Meta:
        verbose_name_plural = "Detalhes"
    
    
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, **kwargs):
        self.nome = self.nome.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = "Clientes"