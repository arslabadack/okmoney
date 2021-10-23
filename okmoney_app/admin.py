from django.contrib import admin

from .models import Produto

# IMPORTAR NOSSOS MODELOS E REGISTRAR NA ADMINISTRAÇÃO djangoadmin

# EXEMPLO


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estque')


admin.site.register(Produto, ProdutoAdmin)
