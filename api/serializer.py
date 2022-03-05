from dataclasses import field, fields
from rest_framework import serializers 
from .models import Cliente, Documento, Categoria, Empresa, Fornecedor, Produto, \
    SubCategoria, Compras, ComprasDetalhe, Venda, VendaDetalhe


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

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empresa
        fields='__all__'
        


class ProdutoSerializer(serializers.ModelSerializer):
    subcat_descricao = serializers.ReadOnlyField(source='subcategoria.descricao')
    class Meta:
        model=Produto
        fields=("id", "codigo", "descricao", "stock", "preco", "subcategoria", "subcat_descricao", "imagem", "thumbnail",)


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'



class ComprasDetalheSerializer(serializers.ModelSerializer):
    produto_descricao = serializers.ReadOnlyField(source='produto.descricao')
    class Meta:
        model=ComprasDetalhe
        fields=["compra", "id", "produto", "quantidade", "preco", "subtotal", "desconto", "total", "produto_descricao"]


class ComprasSerializer(serializers.ModelSerializer):
    detalhe = ComprasDetalheSerializer(many=True, read_only=True)
    print("detalhe", detalhe)

    class Meta:
        model = Compras
        fields = ["id", "fornecedor", "data", "detalhe"]
        #fields = '__all__'


class VendaDetalheSerializer(serializers.ModelSerializer):
    produto_descricao = serializers.ReadOnlyField(source='produto.descricao')
    #produto_imagem = serializers.ImageField(source='produto.imagem') #verificar estava funcionando
    #produ = serializers.ReadOnlyField(source='produto')
    #produto_id = serializers.ReadOnlyField(source='produto.id')
    #produto_completo = ProdutoSerializer(many=False, read_only=True)
    #produto = ProdutoSerializer(many=False, read_only=True)
    class Meta:
        model=VendaDetalhe
        fields=["venda", "id", "produto", "quantidade", "preco", "subtotal", "desconto", "total", "produto_descricao",]






class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        #fields = ["id", "nome", "telefone", "email", "estado"]


class VendaSerializer(serializers.ModelSerializer):
    nome_cliente = serializers.ReadOnlyField(source='cliente.nome')
    cliente = ClienteSerializer(many=False, read_only=True)
    detalhe = VendaDetalheSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = ["id", "cliente", "empresa", "data", "detalhe", "nome_cliente",]
        #fields = '__all__'        