from django.db import models
# from django.db.models.deletion import DO_NOTHING
# from django.contrib.auth.models import User


class MoneyReleases(models.Model):
    date = models.DateTimeField()
    operation = models.BooleanField(default=False)
    reason = models.CharField(max_length=200)
    place = models.CharField(max_length=200, null=True, blank=True)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    observation = models.TextField(max_length=200, null=True, blank=True)


class Meta:
    ordering = ['id']


def __str__(self):
    return self.reason


class reminders(models.Model):
    lembrete = models.CharField('Lembrete', max_length=500, blank=True)

    def __str__(self):
        return self.lembrete


# registered_by = models.ForeignKey(User, on_delete=DO_NOTHING, related_name='registered_by')
