from datetime import date
from django.contrib.messages.storage.fallback import FallbackStorage
from django.http import response
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.test.utils import captured_output
from django.urls import reverse

from okmoney_app.models import *
from okmoney_app.views import *


class MoneyInViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_money_in_view(self):
        request = self.factory.get(reverse('money_in_view'))
        request.user = self.user
        self.assertEqual(response.status_code, 200)
