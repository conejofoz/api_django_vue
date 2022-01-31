from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets 
from .models import ComprasDetelhe, Documento, Categoria, SubCategoria, \
    Produto, Fornecedor, Compras
from .serializer import ComprasSerializer, DocumentoSerializer, CategoriaSerializer, \
    SubCategoriaSerializer, ProdutoSerializer, FornecedorSerializer, \
        ComprasDetalheSerializer


def prueba(request):
    return HttpResponse("primeira vista")



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
    permission_classes = (IsAuthenticated,)
    queryset = Compras.objects.all().order_by('id')    
    serializer_class = ComprasSerializer

class ComprasDetalheViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasDetelhe.objects.all().order_by('id')    
    serializer_class = ComprasDetalheSerializer

    