from django.db import models
# from django.db.models.deletion import DO_NOTHING
# from django.contrib.auth.models import User


# class reminders(models.Model):
#    lembrete = models.CharField('Lembrete', max_length=500, blank=True)

#   def __str__(self):
#      return self.lembrete


class MoneyReleases(models.Model):
    date = models.DateField()
    operation = models.CharField(max_length=100, null=False, blank=False)
    reason = models.CharField(max_length=200)
    place = models.CharField(max_length=200, null=True, blank=True)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    observation = models.TextField(max_length=200, null=True, blank=True)
#    r = models.ForeignKey(reminders, on_delete=models.CASCADE, related_name='r')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f' Data: {self.date}, Operação: {self.operation}, Valor: {self.value}'


class reminders(models.Model):
    date = models.DateField()
    lembrete = models.CharField('Lembrete', max_length=500, blank=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f' Lembrete: {self.lembrete}, Data: {self.date}'


# registered_by = models.ForeignKey(User, on_delete=DO_NOTHING, related_name='registered_by')
