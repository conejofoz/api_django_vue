from unicodedata import name
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import viewsets, status 

from rest_framework.parsers import JSONParser
import json


from .models import ComprasDetalhe, Documento, Categoria, SubCategoria, \
    Produto, Fornecedor, Compras, Cliente, Venda, VendaDetalhe, Empresa
from .serializer import ClienteSerializer, ComprasSerializer, DocumentoSerializer, CategoriaSerializer, \
    SubCategoriaSerializer, ProdutoSerializer, FornecedorSerializer, \
        ComprasDetalheSerializer, VendaSerializer, VendaDetalheSerializer, EmpresaSerializer, VendaSerializerCliente


def index(request):
    return render(request, 'index.html')


def prueba(request):
    return HttpResponse("primeira vista")


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


class EmpresaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Empresa.objects.all().order_by('id')
    serializer_class = EmpresaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all().order_by('descricao')
    serializer_class = CategoriaSerializer


class SubCategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = SubCategoria.objects.all().order_by('descricao')
    serializer_class = SubCategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Produto.objects.all().order_by('descricao')
    serializer_class = ProdutoSerializer

    @action(methods=['get'], detail=False,permission_classes=[], 
        url_path='by-descricao/(?P<descricao>[\w\ ]+)')
    def by_descricao(self, request, pk=None, descricao=None):
        print(descricao)
        obj = Produto.objects.filter(descricao__icontains=descricao)
        print('OBJ: ', obj)
        if not obj:
            return Response({"detail": "Não existe um produto com esse nome"})
        serializador = ProdutoSerializer(obj, many=True)
        print('SERIALIZADOR: ',serializador.data)
        return Response(serializador.data)


class FornecedorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Fornecedor.objects.all().order_by('nome')
    serializer_class = FornecedorSerializer


class ComprasViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Compras.objects.all().order_by('id')    
    serializer_class = ComprasSerializer

class ComprasDetalheViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = ComprasDetalhe.objects.all().order_by('id')    
    serializer_class = ComprasDetalheSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by('nome')
    print('QUERYSET: ', queryset) 
    serializer_class = ClienteSerializer

    @action(methods=['get'], detail=False,permission_classes=[], 
        url_path='by-name/(?P<nome>[\w\ ]+)')
    def by_name(self, request, pk=None, nome=None):
        print(nome)
        obj = Cliente.objects.filter(nome__icontains=nome,estado=True)
        print('OBJ: ', obj)
        if not obj:
            return Response({"detail": "Não existe um cliente com esse nome"})
        serializador = ClienteSerializer(obj, many=True)
        print('SERIALIZADOR: ',serializador.data)
        return Response(serializador.data)


class VendaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Venda.objects.all().order_by('id')    
    serializer_class = VendaSerializer

    def list(self, request, *args, **kwargs):
        queryset = Venda.objects.all()
        serializer = VendaSerializerCliente(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #request.data["cliente_id"] = request.data["cliente"]
        #request.data["cliente_id"] = 500
        serializerVenda = VendaSerializer(data=request.data)
        
        #serializerVenda.create(cliente_id=request.data["cliente_id"])
        print("request.data ==>", request.data)
        #print("cliente ==>", request.data["cliente"])
        if serializerVenda.is_valid():
            serializerVenda.save()
        #else:
            #print('serialize é inválido')
            #return Response("Erro ao serializar o cabeçalho da venda: ")

            numeroVenda = serializerVenda.data['id']
            produtos = json.loads(request.POST.get('produtos'))
            print(produtos)
            for produto in produtos:
                produto['venda'] = numeroVenda
                serializerDetalhe = VendaDetalheSerializer(data=produto)
                if serializerDetalhe.is_valid():
                    serializerDetalhe.save()
                else:
                    print('serialize é inválido')
                    return Response("Erro ao serializar o item da venda: ")
            #return super().create(request, *args, **kwargs)
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