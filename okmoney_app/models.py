from django.db import models


class MoneyIn(models.Model):
    categoria = models.CharField(max_length=100)
    valor = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    observacao = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.nome


class MoneyOut(models.Model):
    categoria = models.CharField('Categoria', max_length=100)
    motivo = models.CharField('Motivo', max_length=200)
    local = models.CharField('Local', max_length=200)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=8)
    data = models.DateField('Data')
    metodo_pagamento = models.models.BooleanField(("Método de Pagamento"))
    observacao = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.motivo


class reminders(models.Model):
    lembrete = models.CharField('Lembrete', max_length=500, blank=True)

    def __str__(self):
        return self.lembrete
