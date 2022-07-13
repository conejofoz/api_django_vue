#from unicodedata import name
from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LancamentoCaixaViewSet, prueba, DocumentoViewSet, \
    CategoriaViewSet, SubCategoriaViewSet, ProdutoViewSet, FornecedorViewSet, \
    CompraViewSet, CompraDetalheViewSet, ClienteViewSet, UserViewSet, \
    VendaViewSet, VendaDetalheViewSet, ContaContabilViewSet, \
    upload, clientest, EmpresaViewSet, MoedaViewSet, email_contato, \
    ajusta_estoque, LancamentoCaixaSimplesViewSet

from .viewsExporta import exporta_categoria, exporta_produto, import_csv

router = routers.DefaultRouter()
router.register(r'docs', DocumentoViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'subcategoria', SubCategoriaViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'fornecedor', FornecedorViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'compras-detalhe', CompraDetalheViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'usuario', UserViewSet)
router.register(r'vendas-detalhe', VendaDetalheViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'moedas', MoedaViewSet)
router.register(r'lancamento-caixa', LancamentoCaixaViewSet)
router.register(r'lancamento-caixa-simples', LancamentoCaixaSimplesViewSet)
router.register(r'conta-contabil', ContaContabilViewSet)
#router.register(r'email-contato', EnviarEmailAPIView)


urlpatterns = [
    # path('', prueba, name='prueba')
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair" ),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh" ),
    path('upload/', upload, name='upload'),
    path('clientest/', clientest, name='clientest'),
    path('email-contato/', email_contato, name='email_contato'),
    path('ajusta-estoque/', ajusta_estoque, name='ajusta_estoque'),
    path('exporta-categoria/', exporta_categoria, name='exporta_categoria'),
    path('import-categoria/', import_csv, name='import_csv'),
    path('exporta-produto/', exporta_produto, name='exporta_produto'),
]
