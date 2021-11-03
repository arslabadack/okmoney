from django.contrib import admin

from .models import *


# class ProdutoAdmin(admin.ModelAdmin):
#    list_display = ('nome', 'preco', 'estque')


# admin.site.register(Produto, ProdutoAdmin)

class MoneyReleaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'operation', 'reason', 'place', 'value',
                    'payment_method', 'observation')


admin.site.register(MoneyReleases, MoneyReleaseAdmin)
