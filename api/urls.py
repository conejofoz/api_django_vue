from unicodedata import name
from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LancamentoCaixaViewSet, prueba, DocumentoViewSet, CategoriaViewSet, \
    SubCategoriaViewSet, ProdutoViewSet, FornecedorViewSet, \
        CompraViewSet, CompraDetalheViewSet, ClienteViewSet, \
            VendaViewSet, VendaDetalheViewSet, \
                 upload, clientest, EmpresaViewSet, MoedaViewSet, email_contato, ajusta_estoque

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
router.register(r'vendas-detalhe', VendaDetalheViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'moedas', MoedaViewSet)
router.register(r'lancamento-caixa', LancamentoCaixaViewSet)
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
]
