from django.test import TestCase
from okmoney_app.forms import *


class MoneyInFormTestCase(TestCase):

    def test_form_is_valid(self):
        form = MoneyInModelForm({
            'date': '01/01/2021',
            'category': 'salario',
            'value': 5000.00,
            'observation': 'observation'
        })
        self.assertTrue(form.is_valid())

    def test_form_is_blank(self):
        form = MoneyInModelForm({
            'date': '01/01/2021',
            'category': 'salario',
            'observation': 'observation'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors, {'value': ['Este campo é obrigatório.'], })


class MoneyOutFormTestCase(TestCase):

    def test_form_is_valid(self):
        form = MoneyOutModelForm({
            'date': '01/01/2021',
            'category': 'impostos',
            'reason': 'motivo_teste',
            'place': 'local_teste',
            'value': 2000.00,
            'payment_method': 'deposito',
            'observation': 'observação_teste'
        })
        self.assertTrue(form.is_valid())

    def test_form_is_blank(self):
        form = MoneyOutModelForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'date': ['Este campo é obrigatório.'],
            'category': ['Este campo é obrigatório.'],
            'reason': ['Este campo é obrigatório.'],
            'place': ['Este campo é obrigatório.'],
            'value': ['Este campo é obrigatório.'],
            'payment_method': ['Este campo é obrigatório.'], })


class FutureFormTestCase(TestCase):

    def test_form_is_valid(self):
        form = FutureModelForm({
            'release_date': '01/01/2021',
            'receiving_date': '02/01/2021',
            'category': 'entrada',
            'reason': 'motivo_teste',
            'value': 100.00,
        })
        self.assertTrue(form.is_valid())

    def test_form_is_blank(self):
        form = FutureModelForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'release_date': ['Este campo é obrigatório.'],
            'receiving_date': ['Este campo é obrigatório.'],
            'category': ['Este campo é obrigatório.'],
            'reason': ['Este campo é obrigatório.'],
            'value': ['Este campo é obrigatório.'], })
