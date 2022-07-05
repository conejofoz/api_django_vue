from django.contrib import admin

from api.models import ContaContabil, LancamentoCaixa, Produto
# Register your models here.


class ContaContabilAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'tipo')

class LancamentoCaixaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'siglaMoeda')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', )

admin.site.register(ContaContabil, ContaContabilAdmin)
admin.site.register(LancamentoCaixa, LancamentoCaixaAdmin)
admin.site.register(Produto, ProdutoAdmin)