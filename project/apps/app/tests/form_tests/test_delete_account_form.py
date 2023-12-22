from django.contrib.auth.models import User
from django.test import TestCase

from project.apps.app.forms import DeleteAccountForm
from project.apps.app.models import Account


class DeleteAccountTestForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
        )
        self.account = Account.objects.create(
            name='Test Account',
            balance=1000.00,
            user=self.user,
        )
        self.data = {
            'account': self.account.id,
        }

    def test_form_with_valid_data(self):
        form = DeleteAccountForm(data=self.data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        self.data.update({'account': 9999})  # Invalid account id
        form = DeleteAccountForm(data=self.data, user=self.user)
        self.assertFalse(form.is_valid())
