# gerar thumbnail
# from ast import Try
# from ctypes import sizeof
# from distutils.command.upload import upload
# from email.mime import image
# from operator import mod, truediv
# from pickletools import optimize
from email.policy import default
from io import BytesIO
from ntpath import realpath
from tabnanny import verbose
# from tkinter import N
# from tabnanny import verbose
# from ssl import Options
# from turtle import width
from django.conf import settings
from django.core.files import File
import os
from django.core.mail import send_mail, mail_admins

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey



from PIL import Image

from api_dj.settings import MEDIA_URL, STATIC_URL, BASE_DIR, MEDIA_ROOT


class ModeloEdit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    uc = UserForeignKey(auto_user_add=True, related_name='+') 
    um = UserForeignKey(auto_user=True, related_name='+')
    # usuario = models.ForeignKey(User, on_delete=models.RESTRICT)

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


class Categoria(ModeloEdit):
    descricao = models.CharField(max_length=50, null=False,blank=False, unique=True)
    
    def __str__(self):
        return self.descricao + ' - id: ' + str(self.pk)

    def save(self, **kwargs):
        novo = self.id
        self.descricao = self.descricao.upper()
        super(Categoria, self).save()

        if novo is None:
            send_mail(
                'Nova categoria cadastrada',
                'A categoria %s foi cadastrada' % self.descricao,
                'infinity@infinity-group.net',
                ['infinity@infinity-group.net', 'conejofoz@gmail.com'],
                fail_silently=False,
            )

            mail_admins(
                'Nova categoria cadastrada',
                'A categoria %s foi cadastrada' % self.descricao,
                fail_silently=False,
            )

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ModeloEdit):
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



class Fornecedor(ModeloEdit):
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

class Grupo(ModeloEdit):
    nome = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):  
        return self.nome

    def save(self, **kwargs):
        self.nome = self.nome.upper()
        super(Grupo, self).save()

    class Meta:
        verbose_name_plural = 'Grupos'


class Produto(ModeloEdit):

    """ def nome_imagem(self, filename):
        extension = os.path.splitext(filename)[-1]
        return '%s/self.codigo%s'%('produtos', extension,) """

    codigo = models.CharField(max_length=10, null=False, blank=False)
    descricao = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)

    qtd1 = models.IntegerField(default=0, blank=True, null=True)
    qtd2 = models.IntegerField(default=0, blank=True, null=True)
    qtd3 = models.IntegerField(default=0, blank=True, null=True)
    qtd4 = models.IntegerField(default=0, blank=True, null=True)
    qtd5 = models.IntegerField(default=0, blank=True, null=True)
    qtd6 = models.IntegerField(default=0, blank=True, null=True)
    qtd7 = models.IntegerField(default=0, blank=True, null=True)
    qtd8 = models.IntegerField(default=0, blank=True, null=True)
    qtd9 = models.IntegerField(default=0, blank=True, null=True)
    
    deposito1 = models.IntegerField(default=0, blank=True, null=True)
    deposito2 = models.IntegerField(default=0, blank=True, null=True)
    deposito3 = models.IntegerField(default=0, blank=True, null=True)
    deposito4 = models.IntegerField(default=0, blank=True, null=True)
    deposito5 = models.IntegerField(default=0, blank=True, null=True)
    deposito6 = models.IntegerField(default=0, blank=True, null=True)
    deposito7 = models.IntegerField(default=0, blank=True, null=True)
    
    preco = models.FloatField(default=0)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.PROTECT)
    #imagem = models.ImageField(null=True, blank=True, upload_to='produtos/')
    #thumbnail = models.ImageField(null=True, blank=True, upload_to='produtos/')
    imagem = models.ImageField(null=True, blank=True, upload_to='')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='')
    empresa = models.ManyToManyField(Empresa, related_name="produtos", through="EstoqueEmpresa", blank=True, default=1)
    
    referencia = models.CharField(max_length=100, blank=True, null=True)
    codigo_origem = models.CharField(max_length=100, blank=True, null=True)
    codigo_barras = models.CharField(max_length=100, blank=True, null=True)
    grupo = models.ForeignKey(Grupo, default=1, related_name="grupos", on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(Fornecedor, default=1, related_name="fornecedores", on_delete=models.PROTECT)
    unidade = models.CharField(max_length=10, blank=True, null=True)
    iva = models.FloatField(default=0, null=True, blank=True)

    # PREÇOS DEPOSTIO
    preco_atacado_dp = models.FloatField(default=0, null=True, blank=True)
    preco_custo_dp = models.FloatField(default=0, null=True, blank=True)
    preco_origem_dp = models.FloatField(default=0, null=True, blank=True)
    preco_ficticio_dp = models.FloatField(default=0, null=True, blank=True)

    preco_medio = models.FloatField(default=0, null=True, blank=True)
    preco_custo = models.FloatField(default=0, null=True, blank=True)
    preco_atacado = models.FloatField(default=0, null=True, blank=True)

    data_ultima_compra = models.DateField(null=True, blank=True)
    data_ultima_venda = models.DateField(null=True, blank=True)
    
    quantidade_por_caixa = models.FloatField(default=0, null=True, blank=True)
    peso_neto_caixa = models.FloatField(default=0, null=True, blank=True)
    peso_bruto_caixa = models.FloatField(default=0, null=True, blank=True)

    descricaodi = models.CharField(max_length=200, null=True, blank=True)
    descricao2di = models.CharField(max_length=200, null=True, blank=True)
    marcadi = models.CharField(max_length=100, null=True, blank=True)
    fabricadi = models.CharField(max_length=100, null=True, blank=True)
    classificacaodi = models.CharField(max_length=100, null=True, blank=True)
    preco_custo_di = models.FloatField(default=0, null=True, blank=True)
    del_foto = models.BooleanField(default=False, null=True, blank=True)

    

    def get_image(self):
        if self.imagem:
            return '{}{}'.format(MEDIA_URL, self.imagem)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def __str__(self):
        return self.descricao

    def __getitem__(self, key):
        return self.__dict__[key]

    def save(self, *args, **kwargs):
        if self.codigo > '':
            nome_img = self.codigo
        else:
            nome_img = self.descricao

        if self.imagem:
            self.imagem.name = u'produtos/'+nome_img+'.%s' % self.imagem.name.split('.')[1] # Pegando a extensão da img
        if self.thumbnail:
            self.thumbnail.name = u'produtos/'+nome_img+'_thumbnail.%s' % self.imagem.name.split('.')[1] # Pegando a extensão da img
        
        if self.id is not None:
            print('apagar foto===================================================: ', self.del_foto)
            if self.del_foto == True:
                try: 
                    img_antiga = os.path.join(settings.MEDIA_ROOT, self.imagem.path)
                    tum_antigo = os.path.join(settings.MEDIA_ROOT, self.thumbnail.path)
                    os.remove(img_antiga)
                    os.remove(tum_antigo)
                    self.del_foto = False
                except Exception as e:
                    print("Error removing", e)
            
        self.descricao = self.descricao.upper()
        #self.thumbnail = self.make_thumbnail(self.imagem)

        print('apagar foto===================================================: ', self.del_foto)
        
        super().save(*args, **kwargs)
        try:
            if self.thumbnail:
                self.resize_image(self.thumbnail.name, 720, 60)
            if self.imagem:
                self.resize_image(self.imagem.name, 1280, 80)
        except Exception as e:
            print("Error resizing image:", e)

    @staticmethod
    def resize_image(img_name, new_width, qualidade):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name) 
        img = Image.open(img_path)
        width, height = img.size
        if new_width == 720:
            #new_height = 480 #405
            new_height = round((new_width * height) / width)
        else:
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


class EstoqueEmpresa(ModeloEdit):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empresa_estoque", blank=True, null=True, default=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="empresa_estoque", blank=True, null=True, default=1)
    quantidade = models.FloatField(default=0)
    deposito1 = models.FloatField(default=0)
    deposito2 = models.FloatField(default=0)
    deposito3 = models.FloatField(default=0)
    deposito4 = models.FloatField(default=0)
    deposito5 = models.FloatField(default=0)
    deposito6 = models.FloatField(default=0)
    deposito7 = models.FloatField(default=0)

    def __st__(self):
        return "{} - {} - ({})".format(self.produto.descricao, self.empresa.nome, self.quantidade)

    class Meta:
        ordering = ['id']


class Compra(ModeloEdit):
    fornecedor = models.ForeignKey(Fornecedor, related_name='fornecedor', on_delete=models.RESTRICT)
    empresa = models.ForeignKey(Empresa, default=1, on_delete=models.RESTRICT)
    data = models.DateField()
    total = models.FloatField(default=0)
    paga = models.BooleanField(default=False)
    origem = models.IntegerField(blank=True, null=True)
    tipo_movimento = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Compras"


class CompraDetalhe(ModeloEdit):
    compra = models.ForeignKey(Compra, related_name='detalhe', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    quantidade = models.IntegerField(default=0)
    preco = models.FloatField(default=0)        
    desconto = models.FloatField(default=0)        
    deposito = models.IntegerField(default=0)
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco

    @property
    def total(self):
        return self.subtotal - self.desconto

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.compra, self.produto)

    class Meta:
        verbose_name_plural = "Detalhes de Compra"
""" 
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
    
 """    


class Cliente(ModeloEdit):
    nome = models.CharField(max_length=200, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='clientes/')

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
    destino = models.IntegerField(blank=True, null=True)
    tipo_movimento = models.IntegerField(blank=True, null=True)

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
    deposito = models.IntegerField(default=0)
    
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

class ContaContabil(ModeloEdit):
    descricao = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=1, null=False, blank=False)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Contas Contábeis'


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
    conta_contabil = models.ForeignKey(ContaContabil, related_name="lancamentos", on_delete=models.RESTRICT)
    comprovante = models.FileField(blank=True, null=True, upload_to='uploads/lancamentos/')
    class Meta:
        verbose_name_plural = 'Lancamentos de caixa'




# Signals de Compra
""" 
@receiver(post_save, sender=CompraDetalhe)
def somar_quantidade(sender, instance, **kwargs):
    id_produto = instance.produto.id 
    produto = Produto.objects.get(id = id_produto)
    
    if produto:
        produto.stock = int(produto.stock) + int(instance.quantidade)
        produto.save()


@receiver(post_delete, sender=CompraDetalhe)
def diminuir_quantidade(sender, instance, **kwargs):
    id_produto = instance.produto.id 
    produto = Produto.objects.filtert(id = id_produto).first()
    
    if produto:
        produto.stock -= int(instance.quantidade)
        produto.save()

 """
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
