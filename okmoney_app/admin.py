from django.contrib import admin

from .models import *


class MoneyInAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'value', 'observation')


admin.site.register(MoneyIn, MoneyInAdmin)


class MoneyOutAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'reason', 'place', 'value',
                    'payment_method', 'observation')


admin.site.register(MoneyOut, MoneyOutAdmin)
