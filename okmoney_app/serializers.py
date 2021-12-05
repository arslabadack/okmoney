from django.db.models import fields
from rest_framework import serializers
from . import models


class MoneyInSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyIn
        fields = (
            'author',
            'date',
            'category',
            'value',
            'observation',
        )


class MoneyOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoneyOut
        fields = (
            'author',
            'date',
            'category',
            'reason',
            'place',
            'value',
            'payment_method',
            'observation',
        )


class FutureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Future
        fields = (
            'author',
            'release_date',
            'receiving_date',
            'category',
            'reason',
            'value',
        )
