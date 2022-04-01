#gerar thumbnail
#from ast import Try
from ctypes import sizeof
#from distutils.command.upload import upload
#from email.mime import image
from io import BytesIO
from operator import mod, truediv
from pickletools import optimize
from tabnanny import verbose
#from ssl import Options
#from turtle import width
from django.conf import settings
from django.core.files import File
import os


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models

from PIL import Image

from api_dj.settings import MEDIA_URL, STATIC_URL, BASE_DIR, MEDIA_ROOT


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


class Empresa(ModeloEdit):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):    
        return self.nome

    def save(self, **kwargs):
        self.nome = self.nome.upper()
        super(Empresa, self).save()

    class Meta:
        verbose_name_plural = "Empresas"


class Categoria(models.Model):
    descricao = models.CharField(max_length=50, null=False,blank=False, unique=True)

    def __str__(self):
        return self.descricao + ' - id: ' + str(self.pk)

    def save(self, **kwargs):
        self.descricao = self.descricao.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='subcategorias', on_delete=models.PROTECT)
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
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.PROTECT)
    imagem = models.ImageField(null=True, blank=True, upload_to='produtos/')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='produtos/')

    def get_image(self):
        if self.imagem:
            return '{}{}'.format(MEDIA_URL, self.imagem)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return self.descricao

    def __getitem__(self, key):
        return self.__dict__[key]

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        #self.thumbnail = self.make_thumbnail(self.imagem)
        super().save(*args, **kwargs)
        if self.thumbnail:
            self.resize_image(self.thumbnail.name, 720, 60)
        if self.imagem:
            self.resize_image(self.imagem.name, 1280, 80)

    @staticmethod
    def resize_image(img_name, new_width, qualidade):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name) 
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width < new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=qualidade)
        new_img.close()
        img.close()

    class Meta:
        verbose_name_plural = "Produtos"

    def make_thumbnail(imagem, size=(300, 200)):
        img = Image.open(imagem)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=imagem.name)

        return thumbnail


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
    imagem = models.ImageField(null=True, blank=True,upload_to='clientes/')

    def get_image(self):
        if self.imagem:
            return '{}{}'.format(MEDIA_URL, self.imagem)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return self.nome

    def save(self, **kwargs):
        self.nome = self.nome.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = "Clientes"


class Venda(ModeloEdit):
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.RESTRICT)
    empresa = models.ForeignKey(Empresa, default=1, on_delete=models.RESTRICT)
    data = models.DateField()
    total = models.FloatField(default=0)
    paga = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Vendas"



class VendaDetalhe(ModeloEdit):
    venda = models.ForeignKey(Venda, related_name='detalhe', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
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
        return '{}-{}-{}'.format(self.id, self.venda, self.produto)

    class Meta:
        verbose_name_plural = "Detalhes de Venda"

    #def save(self, *args, **kwargs):
        #print("**************************************************************")
        #print("produto====>", self.produto_id)
        #self.produto_id = 5
        #super(VendaDetalhe, self).save()


class LancamentoCaixa(ModeloEdit):
    controle = models.CharField(max_length=100, blank=True, null=True)
    data = models.DateField()
    descricao = models.CharField(max_length=200, null=False, blank=False)
    siglaMoeda = models.CharField(max_length=2, blank=False, null=False)
    tipo = models.CharField(max_length=1, null=False, blank=False)
    valor1 = models.FloatField(default=0)
    cotacao = models.FloatField(default=0)
    valor2 = models.FloatField(default=0)
    empresa = models.ForeignKey(Empresa, default=1, on_delete=models.RESTRICT)


# Signals de Compra
@receiver(post_save, sender=ComprasDetalhe)
def somar_quantidade(sender, instance, **kwargs):
    id_produto = instance.produto.id 
    produto = Produto.objects.get(id = id_produto)
    
    if produto:
        produto.stock = int(produto.stock) + int(instance.quantidade)
        produto.save()


@receiver(post_delete, sender=ComprasDetalhe)
def diminuir_quantidade(sender, instance, **kwargs):
    id_produto = instance.produto.id 
    produto = Produto.objects.filtert(id = id_produto).first()
    
    if produto:
        produto.stock -= int(instance.quantidade)
        produto.save()


# Signals de Venda

@receiver(post_save, sender=VendaDetalhe)
def diminuir_qtd(sender, instance, **kwargs):
    id_produto = instance.produto.id 
    produto = Produto.objects.filter(id=id_produto).only('stock').first()
    #produto = Produto.objects.get(id=id_produto)
    if produto:
        print('PRODUTO:->> ', produto)
        produto.stock = int(produto.stock) - int(instance.quantidade)
        """ 
        Estava dando erro por causa do resize imagem no model
        como a venda gravava normal mais estourava um erro
        capiturei a excessão e deixei passar
        """
        try:
            produto.save()
            print("Estoque atualizado: ", produto.stock)
        except Exception as e: 
            print("Deu erro no save do receiver da venda", str(e))


@receiver(post_delete, sender=VendaDetalhe)
def somar_qtd(sender, instance, **kwargs):
    id_produto = instance.produto.id 
    produto = Produto.objects.filter(id=id_produto).first()
    
    if produto:
        produto.stock += int(instance.quantidade)
        try:
           produto.save()
        except Exception as e: 
           print(str(e))


class Moeda(ModeloEdit):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, related_name="moedas")
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3)
    cotacao = models.FloatField(default=0)
    acrescimo = models.FloatField(default=0)

    def __str__(self):
        return self.descricao

    def save(self, **kwargs):
        self.descricao = self.descricao.upper()
        self.sigla  = self.sigla.upper()
        super(Moeda, self).save()

    class Meta:
        verbose_name_plural = "moedas"
        unique_together = ("empresa", "descricao", )
