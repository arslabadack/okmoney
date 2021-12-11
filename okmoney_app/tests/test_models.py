from datetime import date
from django.test import TestCase
from model_mommy import mommy
from okmoney_app.forms import MoneyInModelForm

from okmoney_app.models import *


class MoneyInTestCase(TestCase):

    def setUp(self):
        self.money_in = mommy.make('MoneyIn', category='salario')

    def test_money_in_date(self):
        self.assertEqual(self.money_in.date, date.today())

    def test_money_in_category(self):
        self.assertEqual(str(self.money_in.category), 'salario')

    def test_money_in_value(self):
        self.assertEqual(self.money_in.value, self.money_in.value)

    def test_money_in_observation(self):
        self.assertIsNone(self.money_in.observation, None)


class MoneyOutTestCase(TestCase):

    def setUp(self):
        self.money_out = mommy.make(
            'MoneyOut', category='saude', payment_method='pix')

    def test_money_out_date(self):
        self.assertEqual(self.money_out.date, date.today())

    def test_money_out_category(self):
        self.assertEqual(str(self.money_out.category), 'saude')

    def test_money_out_reason(self):
        self.assertEqual(str(self.money_out.reason), self.money_out.reason)

    def test_money_out_place(self):
        self.assertEqual(str(self.money_out.place), self.money_out.place)

    def test_money_out_value(self):
        self.assertEqual(self.money_out.value, self.money_out.value)

    def test_money_out_payment_method(self):
        self.assertEqual(str(self.money_out.payment_method), 'pix')

    def test_money_out_observation(self):
        self.assertIsNone(self.money_out.observation, None)


class FutureTestCase(TestCase):

    def setUp(self):
        self.future = mommy.make('Future', category='entrada')

    def test_future_release_date(self):
        self.assertEqual(self.future.release_date, date.today())

    def test_future_receiving_date(self):
        self.assertEqual(self.future.receiving_date, date.today())

    def test_future_category(self):
        self.assertEqual(str(self.future.category), 'entrada')

    def test_future_reason(self):
        self.assertEqual(str(self.future.reason), self.future.reason)

    def test_future_value(self):
        self.assertEqual(self.future.value, self.future.value)


class RemindersTestCase(TestCase):

    def setUp(self):
        self.reminder = mommy.make('Reminders')
        print(self.reminder)

    def test_reminder_content(self):
        self.assertEqual(str(self.reminder.content), self.reminder.content)
