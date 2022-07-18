# from dataclasses import field, fields
# from dataclasses import fields
from asyncore import read
from imp import source_from_cache
from importlib.resources import read_binary
from re import M
from django.contrib.auth.models import User
from django.http import QueryDict
from rest_framework import serializers 
from .models import Cliente, Documento, Categoria, Empresa, Fornecedor, \
    LancamentoCaixa, Produto, SubCategoria, Compra, CompraDetalhe, Venda, \
    VendaDetalhe, Moeda, EstoqueEmpresa, ContaContabil


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude = ["password"]
        # fields = ["id", "username"]

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class SubCategoriaSerializerList(serializers.ModelSerializer):

    class Meta:
        model = SubCategoria
        # fields='__all__'
        fields = ("id", "descricao", )

class CategoriaSerializer(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(read_only=True)
    # usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='usuario')
    um = UsuarioSerializer(read_only=True)
    uc = UsuarioSerializer(read_only=True)

    """ 
        subcategorias = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        retorna só o id
        
        a classe SubCategoriaSerializer não se pode usar porque esta definida depois
        para colocar a subcategoria completa na categoria a solução foi criar uma classe serializer só para listar
        e se colocar a subcategoria para cima para de funcionar a categoria que tem dentro dela
        outra coisa muito importante o nome do campo subcategorias é o nome que está em related_name='subcategorias'
            la no model
    """
   
    # usando outro serializer só para listagem    
    subcategorias = SubCategoriaSerializerList(read_only=True, many=True)
    
    class Meta:
        model = Categoria
        fields = '__all__'
        # fields = ("id", "descricao", "subcategorias")
        # fields = ("id", "descricao", "usuario", "usuario_id", "uc", "um")


class SubCategoriaSerializer(serializers.ModelSerializer):
    # categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    # categoria = serializers.StringRelatedField()
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), write_only=True, source='categoria')
    cat_descricao = serializers.ReadOnlyField(source='categoria.descricao')

    class Meta:
        model = SubCategoria
        # fields='__all__'
        fields = ("id", "descricao", "cat_descricao", "categoria", "categoria_id")


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class EstoqueEmpresaSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.ReadOnlyField(source="empresa.nome")
    produto_descricao = serializers.ReadOnlyField(source="produto.descricao")

    class Meta:
        model = EstoqueEmpresa
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    subcat_descricao = serializers.ReadOnlyField(source='subcategoria.descricao')
    estoque_empresa = EstoqueEmpresaSerializer(many=True, read_only=True, source="empresa_estoque")

    class Meta:
        model = Produto
        fields = (
            "id", "codigo", "descricao", "stock", "preco", "subcategoria", 
            "subcat_descricao", "imagem", "thumbnail", "estoque_empresa",
            "referencia", "codigo_origem", "codigo_barras", "unidade", "iva",
            "quantidade_por_caixa", "peso_neto_caixa", "peso_bruto_caixa",
            "descricaodi", "descricao2di", "marcadi", "fabricadi", "preco_custo_di",
            "preco_atacado_dp", "preco_custo_dp", "preco_origem_dp", "preco_ficticio_dp",
            "preco_medio", "preco_custo", "preco_atacado",
            "del_foto"
             )


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class CompraDetalheSerializer(serializers.ModelSerializer):
    produto_descricao = serializers.ReadOnlyField(source='produto.descricao')

    class Meta:
        model = CompraDetalhe
        fields = ["compra", "id", "produto", "quantidade", "preco", "subtotal", "desconto", "total", "produto_descricao", "deposito",]


class CompraSerializer(serializers.ModelSerializer):
    nome_fornecedor = serializers.ReadOnlyField(source='fornecedor.nome')
    detalhe = CompraDetalheSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ["id", "fornecedor", "empresa", "data", "detalhe", "nome_fornecedor", "total", "paga", "origem", "tipo_movimento"]
        # fields = '__all__'        


class CompraSerializerFornecedor(serializers.ModelSerializer):
    nome_fornecedor = serializers.ReadOnlyField(source='fornecedor.nome')
    fornecedor = FornecedorSerializer(many=False, read_only=True)
    detalhe = CompraDetalheSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ["id", "fornecedor", "empresa", "data", "detalhe", "nome_fornecedor", "total", "paga"]
        # fields = '__all__'      


""" 
class ComprasDetalheSerializer(serializers.ModelSerializer):
    produto_descricao = serializers.ReadOnlyField(source='produto.descricao')
    class Meta:
        model=ComprasDetalhe
        fields=["compra", "id", "produto", "quantidade", "preco", "subtotal", "desconto", "total", "produto_descricao"]


class ComprasSerializer(serializers.ModelSerializer):
    detalhe = ComprasDetalheSerializer(many=True, read_only=True)
    # ###print("detalhe", detalhe)

    class Meta:
        model = Compras
        fields = ["id", "fornecedor", "data", "detalhe"]
        #fields = '__all__'

 """


class VendaDetalheSerializer(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(read_only=True)
    # usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='usuario')
    um = UsuarioSerializer(read_only=True)
    uc = UsuarioSerializer(read_only=True)
    produto_descricao = serializers.ReadOnlyField(source='produto.descricao')
    # produto_imagem = serializers.ImageField(source='produto.imagem') #verificar estava funcionando
    # produ = serializers.ReadOnlyField(source='produto')
    # produto_id = serializers.ReadOnlyField(source='produto.id')
    # produto_completo = ProdutoSerializer(many=False, read_only=True)
    # produto = ProdutoSerializer(many=False, read_only=True)

    class Meta:
        model = VendaDetalhe
        fields = ["venda", "id", "produto", "quantidade", "preco", "subtotal", "desconto", "total", "produto_descricao", "deposito", "uc", "um"]






class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
        # fields = ["id", "nome", "telefone", "email", "estado", "imagem"]


class VendaSerializer(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(read_only=True)
    # usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='usuario')
    um = UsuarioSerializer(read_only=True)
    uc = UsuarioSerializer(read_only=True)

    nome_cliente = serializers.ReadOnlyField(source='cliente.nome')
    detalhe = VendaDetalheSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = ["id", "cliente", "empresa", "data", "detalhe", "nome_cliente", "total", "paga", "destino", "tipo_movimento", "uc", "um", "numero_nf", "extenso"]
        # fields = '__all__'        


class VendaSerializerCliente(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(read_only=True)
    # usuario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='usuario')
    um = UsuarioSerializer(read_only=True)
    uc = UsuarioSerializer(read_only=True)
    nome_cliente = serializers.ReadOnlyField(source='cliente.nome')
    cliente = ClienteSerializer(many=False, read_only=True)
    detalhe = VendaDetalheSerializer(many=True, read_only=True)
    # nome_usuario = serializers.ReadOnlyField(source="user.username")
    usuario = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Venda
        fields = ["id", "usuario", "cliente", "empresa", "data", "detalhe", "nome_cliente", "total", "paga", "destino", "tipo_movimento", "uc", "um", "numero_nf", "extenso"]
        # fields = '__all__'              


class MoedaSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all(), write_only=True, source='empresa')

    class Meta:
        model = Moeda
        fields = ("id", "descricao", "sigla", "cotacao", "acrescimo", "empresa", "empresa_id", )


class ContaContabilSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContaContabil
        fields = ("id", "descricao", "tipo")


class LancamentoCaixaSerializer(serializers.ModelSerializer):
    conta_contabil = ContaContabilSerializer(read_only=True)
    conta_contabil_id = serializers.PrimaryKeyRelatedField(queryset=ContaContabil.objects.all(), write_only=True, source='conta_contabil')

    class Meta:
        model = LancamentoCaixa
        fields = '__all__'

        # fields = ["id", "descricao", ""]





class LancamentoCaixaSimplesSerializer(serializers.ModelSerializer):
    pass
    """ 
    conta_contabil = ContaContabilSerializer(read_only=True)
    conta_contabil_id = serializers.PrimaryKeyRelatedField(queryset=ContaContabil.objects.all(), write_only=True, source='conta_contabil')
    
    class Meta:
        model = LancamentoCaixa
        #fields = '__all__'
        fields = ["id", "cotacao", "tipo", "controle","descricao", "valor1", "valor2", "data", "siglaMoeda", "conta_contabil", "conta_contabil_id", "empresa"]

 """