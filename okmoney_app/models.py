from django.db import models

# exemplo de implementação de uma classe produto no bando de dados


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estque = models.IntegerField('Quantidade em estoque')
# classe que exibe os nomes no admin

    def __str__(self):
        return self.nome
