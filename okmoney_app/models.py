from django.db import models
from users.models import *
from django.conf import settings
from django.contrib.auth.models import User


class MoneyIn(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=100, null=False, blank=False)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    observation = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f' Data: {self.date}, Categoria: {self.category}, Valor: {self.value}'


class MoneyOut(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    date = models.DateField()
    date = models.DateField()
    category = models.CharField(max_length=100, null=False, blank=False)
    reason = models.CharField(max_length=200)
    place = models.CharField(max_length=200, null=True, blank=True)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    observation = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f' Data: {self.date}, Operação: {self.operation}, Valor: {self.value}'


class Future(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    release_date = models.DateField()
    receiving_date = models.DateField()
    category = models.CharField(max_length=100, null=False, blank=False)
    reason = models.CharField('Lembrete', max_length=500, blank=False)
    value = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f' Motivo: {self.reason}, Data de Recebimento: {self.receiving_date}'
