from urllib import response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets 
from .models import ComprasDetalhe, Documento, Categoria, SubCategoria, \
    Produto, Fornecedor, Compras, Cliente, Venda, VendaDetalhe
from .serializer import ClienteSerializer, ComprasSerializer, DocumentoSerializer, CategoriaSerializer, \
    SubCategoriaSerializer, ProdutoSerializer, FornecedorSerializer, \
        ComprasDetalheSerializer, VendaSerializer, VendaDetalheSerializer


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


class CategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all().order_by('descricao')
    serializer_class = CategoriaSerializer


class SubCategoriaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = SubCategoria.objects.all().order_by('descricao')
    serializer_class = SubCategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Produto.objects.all().order_by('descricao')
    serializer_class = ProdutoSerializer


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
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer


class VendaViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Venda.objects.all().order_by('id')    
    serializer_class = VendaSerializer

class VendaDetalheViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = VendaDetalhe.objects.all().order_by('id')    
    serializer_class = VendaDetalheSerializer