from dataclasses import field, fields
from rest_framework import serializers 
from .models import Documento, Categoria, Fornecedor, Produto, \
    SubCategoria


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields='__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
    cat_descricao = serializers.ReadOnlyField(source='categoria.descricao')
    class Meta:
        model=SubCategoria
        #fields='__all__'
        fields = ("id", "categoria", "descricao", "cat_descricao",)


class CategoriaSerializer(serializers.ModelSerializer):
    subcategorias = SubCategoriaSerializer(many=True, read_only=True)
    
    class Meta:
        model=Categoria
        #fields='__all__'
        fields = ("id", "descricao", "subcategorias")


class ProdutoSerializer(serializers.ModelSerializer):
    subcat_descricao = serializers.ReadOnlyField(source='subcategoria.descricao')
    class Meta:
        model=Produto
        fields=("id", "codigo", "descricao", "stock", "preco", "subcategoria", "subcat_descricao")


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'