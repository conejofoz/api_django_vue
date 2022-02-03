from unicodedata import name
from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import prueba, DocumentoViewSet, CategoriaViewSet, \
    SubCategoriaViewSet, ProdutoViewSet, FornecedorViewSet, \
        ComprasViewSet, ComprasDetalheViewSet, ClienteViewSet, \
            VendaViewSet, VendaDetalheViewSet

router = routers.DefaultRouter()
router.register(r'docs', DocumentoViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'subcategoria', SubCategoriaViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'fornecedor', FornecedorViewSet)
router.register(r'compras', ComprasViewSet)
router.register(r'compras-detalhe', ComprasDetalheViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'vendas-detalhe', VendaDetalheViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    #path('', prueba, name='prueba')
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair" ),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh" ),
]
