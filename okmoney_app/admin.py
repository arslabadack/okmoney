from django.contrib import admin

from .models import *


class MoneyReleaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'operation', 'reason', 'place', 'value',
                    'payment_method', 'observation')


admin.site.register(MoneyReleases, MoneyReleaseAdmin)
