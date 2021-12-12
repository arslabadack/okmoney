from django.test import TestCase, RequestFactory, client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

from okmoney_app.models import MoneyIn as MoneyInModel
from okmoney_app.models import MoneyOut as MoneyOutModel
from django.test import Client
from okmoney_app.views import *


class MoneyInViewTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username='user_test',
            password='password_test',
        )
        self.client = Client()
        self.client.login(username='user_test', password='password_test')

    def test_money_in(self):
        dados = {
            'date': '01/01/2021',
            'category': 'salario',
            'value': 1000,
            'observation': 'test',
        }

        response = self.client.post(reverse('moneyin'), dados)
        self.assertEqual(response.status_code, 302)
        self.assertIs(MoneyInModel.objects.all().count(), 1)


class MoneyOutViewTestCase(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username='user_test',
            password='password_test',
        )
        self.client = Client()
        self.client.login(username='user_test', password='password_test')

    def test_money_out(self):
        dados = {
            'date': '01/01/2021',
            'category': 'saude',
            'reason': 'reason_test',
            'place': 'place_test',
            'value': 1000,
            'payment_method': 'pix',
            'observation': 'test',
        }

        response = self.client.post(reverse('moneyout'), dados)
        self.assertEqual(response.status_code, 302)
        self.assertIs(MoneyOutModel.objects.all().count(), 1)
