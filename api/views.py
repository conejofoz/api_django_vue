# from unicodedata import name
import logging
from urllib import request
logger = logging.getLogger('django')

from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import viewsets, status 

from rest_framework.parsers import JSONParser
import json
from rest_framework import pagination

from datetime import date
from datetime import datetime

from .models import CompraDetalhe, Documento, Categoria, EstoqueEmpresa, \
    LancamentoCaixa, SubCategoria, Produto, Fornecedor, Compra, Cliente, \
    Venda, VendaDetalhe, Empresa

from .serializer import ClienteSerializer, CompraSerializer, \
    DocumentoSerializer, CategoriaSerializer, LancamentoCaixaSerializer, \
    MoedaSerializer, SubCategoriaSerializer, ProdutoSerializer, \
    FornecedorSerializer, CompraDetalheSerializer, VendaSerializer, \
    VendaDetalheSerializer, EmpresaSerializer, VendaSerializerCliente, \
    Moeda, CompraSerializerFornecedor, UsuarioSerializer



def index(request):
    return render(request, 'index.html')


def prueba(request):
    return HttpResponse("primeira vista")

@method_decorator(csrf_exempt) 
def email_contato(request):
    email = request.POST
    email_contato = email['nome']
    email_assunto = email['assunto']
    email_mensagem = email['mensagem']
    email_from = email['email_from']
    email_to = 'infinity@infinity-group.net'
    email_tecnico = 'site@infinity-group.net'

    """ send_mail(
     email_assunto,
     email_mensagem,
     email_from,
     [email_to],
     fail_silently=False,
    ) """

    email_obj = EmailMessage(
        email_assunto,
        email_mensagem,
        email_to, # from
        [email_to, email_from, email_tecnico ],
        #reply_to=[email_from],
        #headers={'Message-ID': 'foo'},
        headers={'Reply-To': email_from},
    )

    email_obj.send(fail_silently=False)

    print('Email enviado', email)
    return HttpResponse("resposta do email")


@method_decorator(csrf_exempt) 
def ajusta_estoque(request):
    produtos = Produto.objects.all()
    contador = 1
    empresa = '2'
    empresas = [
        {'empresa': '1', 'antiga': '0'},
        {'empresa': '2', 'antiga': '2'},
        {'empresa': '3', 'antiga': '8'}
    ]
    
    deposito = '7'

    for emp in empresas:
        print(emp, emp['empresa'], emp['antiga'])
        contador = 0
        
        for produto in produtos:
            p = produto
            estoque = p.empresa_estoque.filter(empresa_id=emp['empresa']).first()
            if estoque is not None:
                if emp['empresa'] == '1':
                    estoque.deposito1 = produto['deposito1']
                    estoque.deposito2 = produto['deposito2']
                    estoque.deposito3 = produto['deposito3']
                    estoque.deposito4 = produto['deposito4']
                    estoque.deposito5 = produto['deposito5']
                    estoque.deposito6 = produto['deposito6']
                    estoque.deposito7 = produto['deposito7']
                else:    
                    estoque.quantidade = produto['qtd'+emp['antiga']]
                estoque.save()
            else:
                if emp['empresa'] == '1':
                    EstoqueEmpresa.objects.create(
                        empresa_id=int(emp['empresa']),
                        produto_id=produto['id'],
                        deposito1=produto['deposito1'],
                        deposito2=produto['deposito2'],
                        deposito3=produto['deposito3'],
                        deposito4=produto['deposito4'],
                        deposito5=produto['deposito5'],
                        deposito6=produto['deposito6'],
                        deposito7=produto['deposito7'],
                    )
                else:
                    EstoqueEmpresa.objects.create(
                        empresa_id=int(emp['empresa']),
                        produto_id=produto['id'],
                        quantidade=produto['qtd'+emp['antiga']],
                    )
            contador = contador+1
            print(contador)
    return HttpResponse("terminou...")


@method_decorator(csrf_exempt) 
def ajusta_estoque_odl(request):
    produtos = Produto.objects.all()
    contador = 1
    empresa = '2'
    for produto in produtos:
        p = produto
        estoque = p.empresa_estoque.filter(empresa_id = empresa).first()
        if estoque is not None:
            estoque.quantidade = produto['qtd'+empresa]
            estoque.save()
        else:
            EstoqueEmpresa.objects.create(
                empresa_id=empresa,
                produto_id=produto['id'],
                quantidade=produto['qtd'+empresa] 
            )
        contador=contador+1
        print(contador)
    return HttpResponse("terminou...")



@method_decorator(csrf_exempt) 
def upload(request):
    id = request.POST.get('codigo')
    cliente = Cliente.objects.filter(pk=id).first()
    cliente.imagem = request.FILES['imagem']
    cliente.save()
    return HttpResponse("Passou no upload")
    #return HttpResponse(request)


@method_decorator(csrf_exempt) 
def clientest(request):
    clientes = Cliente.objects.all().order_by('nome')
    data = [
        {
            'id': cliente.id, 
            'nome': cliente.nome, 
            'telefone': cliente.telefone,
            'email': cliente.email,
            'estado':cliente.estado,
            'imagem':cliente.get_image(),
            #'imagem':None,
        }
        for cliente in clientes
    ]
    response = {'dados': data}
    return JsonResponse(response)


class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Documento.objects.all().order_by('id')
    serializer_class = DocumentoSerializer


class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = User.objects.all().order_by('username')
    serializer_class = UsuarioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Empresa.objects.all().order_by('id')
    serializer_class = EmpresaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Categoria.objects.all().order_by('descricao')
    serializer_class = CategoriaSerializer

    def list(self, Request, *args, **kwargs):
        usuario = Request.user.username
        logger.info(usuario + ' Acessou Categoria')
        #queryset = Categoria.objects.all().order_by('descricao')
        #serializer = CategoriaSerializer(queryset, many=True)
        #return Response(serializer.data)
        return super(CategoriaViewSet, self).list(Request, *args, **kwargs)

    def create(self, Request, *args, **kwargs):
        usuario = Request.user.username
        obj = Request.data['descricao']
        logger.info(usuario + ' criou categoria ' + obj )
        return super(CategoriaViewSet, self).create(Request, *args, **kwargs)



class SubCategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    #permission_classes = (DjangoModelPermissions,)
    queryset = SubCategoria.objects.all().order_by('descricao')
    serializer_class = SubCategoriaSerializer


class Paginacao(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = 'page_size'
	max_page_size = 50 #no caso de algum engraçadinho definir 100.000 no front    


class ProdutoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Produto.objects.all().order_by('descricao')
    serializer_class = ProdutoSerializer
    #pagination_class = Paginacao

    def create(self, request, *args, **kwargs):
        estoque_empresa = json.loads(request.POST.get('estoque_empresa'))
        print("estoque_empresa: ---------->", estoque_empresa)
        print(estoque_empresa['produto'])
        print(estoque_empresa['empresa'])
        print(estoque_empresa['quantidade'])
        serializerProduto = ProdutoSerializer(data=request.data)
        print('serializerproduto data',  serializerProduto)
        print("request.data ==>", request.data)
        if serializerProduto.is_valid():
            serializerProduto.save()
            print('\ndpoisde slavar\n', serializerProduto.data)
            print('\n id dpoisde slavar\n', serializerProduto.data['id'])
            EstoqueEmpresa.objects.create(empresa_id=estoque_empresa['empresa'], produto_id=serializerProduto.data['id'])
            print('\ndpoisde slavar\n', serializerProduto.data)
            return Response(serializerProduto.data, status=status.HTTP_201_CREATED)

        return Response(serializerProduto.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False,permission_classes=[], 
        url_path='by-descricao/(?P<descricao>[-\w\ ]+)')
    def by_descricao(self, request, pk=None, descricao=None):
        print('DESCRICAO: ', descricao)
        if descricao == 'vazio':
            print('BUSCA VAZIA')
            #obj = Produto.objects.all().exclude(imagem__isnull=True).order_by('?')[0:90]
            obj = Produto.objects.exclude(imagem__isnull=True).exclude(imagem__iexact='').order_by('?')[0:90]
        else:
            obj = Produto.objects.filter(descricao__icontains=descricao).order_by('descricao')
        print('OBJ: ', obj)
        if not obj:
            return Response({"detail": "Não existe um produto com esse nome"})
        serializador = ProdutoSerializer(obj, many=True)
        print('SERIALIZADOR: ',serializador.data)
        return Response(serializador.data)

    @action(methods=['get'], detail=False,permission_classes=[], 
        url_path='by-subcategoria/(?P<subcategoria>[\w\ ]+)')
    def by_subcategoria(self, request, pk=None, subcategoria=None):
        print(subcategoria)
        obj = Produto.objects.filter(subcategoria_id=subcategoria)
        print('OBJ: ', obj)
        if not obj:
            return Response({"detail": "Não existe um produto com essa subcategoria"})
        serializador = ProdutoSerializer(obj, many=True)
        print('SERIALIZADOR: ',serializador.data)
        return Response(serializador.data)


class FornecedorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fornecedor.objects.all().order_by('nome')
    serializer_class = FornecedorSerializer


class CompraViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Compra.objects.all().order_by('-id')    
    serializer_class = CompraSerializer

    def list(self, request, *args, **kwargs):
        print('o que tem no request',  request.GET)
        print('data inicial: ', request.GET.get('dataInicial'))
        print('data final  : ', request.GET.get('dataFinal'))
        hoje = request.GET.get('dataInicial')
        amanha = request.GET.get('dataFinal')
        empresa = request.GET.get('empresa')
        print('hoje', hoje)
        # queryset = Compra.objects.filter(data='2022-03-11')
        if hoje is None:
            # queryset = Compra.objects.all().order_by('-id')
            queryset = Compra.objects.filter(empresa_id=empresa).order_by('-id')
        else:
            data_atual_servidor = date.today()
            # queryset = Compra.objects.filter(data=hoje)
            if datetime.strptime(hoje, '%Y-%m-%d').date() > data_atual_servidor:
                return Response("Data Inicial não pode ser maior que hoje", status=status.HTTP_400_BAD_REQUEST) 
            if amanha is None:
                amanha = hoje
            if hoje > amanha:
                return Response("Data Inicial não pode ser maior que data final", status=status.HTTP_400_BAD_REQUEST) 
            # queryset = Compra.objects.filter(data__range=(hoje, amanha))
            queryset = Compra.objects.filter(data__range=(hoje, amanha), empresa_id=empresa)

        serializer = CompraSerializerFornecedor(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializerCompra = CompraSerializer(data=request.data)
        empresa = request.data["empresa"]
        print("request.data ==>", request.data)
        # print("cliente ==>", request.data["cliente"])
        if serializerCompra.is_valid():
            serializerCompra.save()
        # else:
            # print('serialize é inválido')
            # return Response("Erro ao serializar o cabeçalho da venda: ")

            numeroCompra = serializerCompra.data['id']
            produtos = json.loads(request.POST.get('produtos'))
            print(produtos)
            for produto in produtos:
                produto['compra'] = numeroCompra
                print('produto com a compra: ', produto)
                serializerDetalhe = CompraDetalheSerializer(data=produto)
                if serializerDetalhe.is_valid():
                    serializerDetalhe.save()
                    p = Produto.objects.get(pk=produto['id'])
                    x = p.empresa_estoque.filter(empresa=empresa).first()
                    print('\n\no x \n', x)
                    if x is not None:
                        # estoque existe, atualizar
                        print('ATUALIZANDO ESTOQUE')
                        if empresa == '1':
                            deposito = produto['deposito']
                            if deposito == 1:
                                x.deposito1 += float(produto['quantidade'])
                            if deposito == 2:
                                x.deposito2 += float(produto['quantidade'])
                            if deposito == 3:
                                x.deposito3 += float(produto['quantidade'])
                            if deposito == 4:
                                x.deposito4 += float(produto['quantidade'])
                            if deposito == 5:
                                x.deposito5 += float(produto['quantidade'])
                            if deposito == 6:
                                x.deposito6 += float(produto['quantidade'])
                            if deposito == 7:
                                x.deposito7 += float(produto['quantidade'])
                        else:
                            x.quantidade += float(produto['quantidade'])
                        
                        x.save()
                    else:
                        # estoque não existe, criar o estoque    
                        print('CRIANDO ESTOQUE')
                        if empresa == '1':
                            deposito = produto['deposito']
                            if deposito == 1:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito1=float(produto['quantidade']) * 1)
                            if deposito == 2:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito2=float(produto['quantidade']) * 1)
                            if deposito == 3:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito3=float(produto['quantidade']) * 1)
                            if deposito == 4:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito4=float(produto['quantidade']) * 1)
                            if deposito == 5:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito5=float(produto['quantidade']) * 1)
                            if deposito == 6:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito6=float(produto['quantidade']) * 1)
                            if deposito == 7:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito7=float(produto['quantidade']) * 1)
                        else:
                            EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], quantidade=float(produto['quantidade']) * 1)
                else:
                    print('serialize é inválido')
                    return Response("Erro ao serializar o item da COMPRA: ")
            return Response(serializerCompra.data, status=status.HTTP_201_CREATED)

        return Response(serializerCompra.errors, status=status.HTTP_400_BAD_REQUEST)  


class CompraDetalheViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = CompraDetalhe.objects.all().order_by('id')    
    serializer_class = CompraDetalheSerializer

"""     def create(self, request):
        serializer = CompraDetalheSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            prod = Produto.objects.get(pk=data["produto"])
            if int(prod.stock) >= int(data["quantidade"]):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Não tem quantidade suficiente" + "Estoque atual: " + str(prod.stock))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 """
""" 
class ComprasViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Compras.objects.all().order_by('id')    
    serializer_class = ComprasSerializer


class ComprasDetalheViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ComprasDetalhe.objects.all().order_by('id')    
    serializer_class = ComprasDetalheSerializer

 """
class ClienteViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by('nome')
    # ###print('QUERYSET: ', queryset) #ESTAVA DANDO PAU NA HORA DE CRIAR UM BANCO NOVO
    serializer_class = ClienteSerializer

    @action(methods=['get'], detail=False, permission_classes=[],
        url_path='by-name/(?P<nome>[\w\ ]+)')
    def by_name(self, request, pk=None, nome=None):
        print(nome)
        obj = Cliente.objects.filter(nome__icontains=nome, estado=True)
        print('OBJ: ', obj)
        if not obj:
            return Response({"detail": "Não existe um cliente com esse nome"})
        serializador = ClienteSerializer(obj, many=True)
        print('SERIALIZADOR: ',serializador.data)
        return Response(serializador.data)


class VendaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Venda.objects.all().order_by('-id')    
    serializer_class = VendaSerializer

    def list(self, Request, *args, **kwargs):
        print('o que tem no request',  Request.query_params)
        print('o que tem no request',  Request)
        #print('o que tem no request',  request.GET)
        #print('data inicial: ', request.GET.get('dataInicial'))
        #print('data final  : ', request.GET.get('dataFinal'))
        #hoje = request.GET.get('dataInicial')
        hoje = Request.query_params['dataInicial']
        #amanha = request.GET.get('dataFinal')
        amanha = Request.query_params['dataFinal']
        #empresa = request.GET.get('empresa')
        empresa = Request.query_params['empresa']
        tipo_movimento = Request.query_params['tipo_movimento']
        #print('hoje', hoje)
        # queryset = Venda.objects.filter(data='2022-03-11')
        if hoje is None:
            # queryset = Venda.objects.all().order_by('-id')
            queryset = Venda.objects.filter(empresa_id=empresa).order_by('-id')
        else:
            data_atual_servidor = date.today()
            # queryset = Venda.objects.filter(data=hoje)
            if datetime.strptime(hoje, '%Y-%m-%d').date() > data_atual_servidor:
                return Response("Data Inicial não pode ser maior que hoje", status=status.HTTP_400_BAD_REQUEST) 
            if amanha is None:
                amanha = hoje
            if hoje > amanha:
                return Response("Data Inicial não pode ser maior que data final", status=status.HTTP_400_BAD_REQUEST) 
            # queryset = Venda.objects.filter(data__range=(hoje, amanha))
            queryset = Venda.objects.filter(data__range=(hoje, amanha), empresa_id=empresa, tipo_movimento=tipo_movimento)
        serializer = VendaSerializerCliente(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializerVenda = VendaSerializer(data=request.data)
        empresa = request.data["empresa"]
        print("request.data ==>", request.data)
        # print("cliente ==>", request.data["cliente"])
        if serializerVenda.is_valid():
            serializerVenda.save()
        # else:
            # print('serialize é inválido')
            # return Response("Erro ao serializar o cabeçalho da venda: ")

            numeroVenda = serializerVenda.data['id']
            produtos = json.loads(request.POST.get('produtos'))
            print(produtos)
            for produto in produtos:
                produto['venda'] = numeroVenda
                print('produto com a venda: ', produto)
                serializerDetalhe = VendaDetalheSerializer(data=produto)
                if serializerDetalhe.is_valid():
                    serializerDetalhe.save()
                    p = Produto.objects.get(pk=produto['id'])
                    x = p.empresa_estoque.filter(empresa=empresa).first()
                    print('\n\no x \n', x)
                    if x is not None:
                        if empresa == '1':
                            deposito = produto['deposito']
                            if deposito == 1:
                                x.deposito1 -= float(produto['quantidade'])
                            if deposito == 2:
                                x.deposito2 -= float(produto['quantidade'])
                            if deposito == 3:
                                x.deposito3 -= float(produto['quantidade'])
                            if deposito == 4:
                                x.deposito4 -= float(produto['quantidade'])
                            if deposito == 5:
                                x.deposito5 -= float(produto['quantidade'])
                            if deposito == 6:
                                x.deposito6 -= float(produto['quantidade'])
                            if deposito == 7:
                                x.deposito7 -= float(produto['quantidade'])
                        else:
                            x.quantidade -= float(produto['quantidade'])
                        
                        x.save()
                    else:
                        # criar o estoque    
                        if empresa == '1':
                            deposito = produto['deposito']
                            if deposito == 1:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito1=float(produto['quantidade']) * -1)
                            if deposito == 2:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito2=float(produto['quantidade']) * -1)
                            if deposito == 3:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito3=float(produto['quantidade']) * -1)
                            if deposito == 4:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito4=float(produto['quantidade']) * -1)
                            if deposito == 5:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito5=float(produto['quantidade']) * -1)
                            if deposito == 6:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito6=float(produto['quantidade']) * -1)
                            if deposito == 7:
                                EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], deposito7=float(produto['quantidade']) * -1)
                        else:
                            EstoqueEmpresa.objects.create(empresa_id=empresa, produto_id=produto['id'], quantidade=float(produto['quantidade']) * -1)
                #else:
                    #print('serialize é inválido')
                    #return Response("Erro ao serializar o item da venda: ")
            return Response(serializerVenda.data, status=status.HTTP_201_CREATED)

        return Response(serializerVenda.errors, status=status.HTTP_400_BAD_REQUEST)  


class VendaDetalheViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = VendaDetalhe.objects.all().order_by('id')    
    serializer_class = VendaDetalheSerializer

    def create(self, request):
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(request.data)
        print('Tipo do request.data ', type(request.data))
        serializer = VendaDetalheSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            prod = Produto.objects.get(pk=data["produto"])
            if int(prod.stock) >= int(data["quantidade"]):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Não tem quantidade suficiente" + "Estoque atual: " + str(prod.stock))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoedaViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Moeda.objects.all().order_by('descricao')
    serializer_class = MoedaSerializer

    def list(self, request, *args, **kwargs):
        print('o que tem no request de moedas',  request.GET)
        empresa = request.GET.get('empresa')
        if empresa is None:
            print("empresa none")
            queryset = Moeda.objects.all().order_by('descricao')
        else:
            print('empresa', empresa)
            queryset = Moeda.objects.filter(empresa_id=empresa).order_by('descricao')    
        serializer = MoedaSerializer(queryset, many=True)
        return Response(serializer.data)


class LancamentoCaixaViewSet(viewsets.ModelViewSet):
    queryset = LancamentoCaixa.objects.all().order_by('descricao')
    serializer_class = LancamentoCaixaSerializer

    def create(self, request, *args, **kwargs):
        print('request->', request.data)
        lista_lancamentos = json.loads(request.POST.get('lancamentos'))
        vendas = json.loads(request.POST.get('vendas'))
        print('lancamentos->', lista_lancamentos)
        for lancamento in lista_lancamentos:
            serializador = LancamentoCaixaSerializer(data=lancamento)
            if serializador.is_valid():
                serializador.save()
            else:
                print('serialize é inválido')
                print('Lançamento=>', lancamento)
                return Response("Erro ao serializar o lancamento: ")
        for numero_venda in vendas:
            venda = Venda.objects.get(pk=numero_venda)
            print('paga ', venda.id, venda.paga)
            venda.paga = True
            venda.save()
        return Response(serializador.data, status=status.HTTP_201_CREATED)
    
        #return super().create(request, *args, **kwargs)

        # return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)