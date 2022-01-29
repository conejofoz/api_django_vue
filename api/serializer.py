from rest_framework import serializers 
from .models import Documento, Categoria, \
    SubCategoria


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documento
        fields='__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
    cat_descricao = serializers.ReadOnlyField(source='categoria.descricao')
    class Meta:
        model=SubCategoria
        #fields='__all__'
        fields = ("id", "categoria", "descricao", "cat_descricao")