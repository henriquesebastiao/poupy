from django.contrib.auth.models import User
from django.test import TestCase

from project.apps.app.forms import NewTransactionForm
from project.apps.app.models import Account


class NewTransactionTestForm(TestCase):
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
            'description': 'Test Transaction',
            'account': self.account.id,
            'value': 100.00,
        }

    def mixin_validate_form(self, string_to_validate: str, *args: str) -> NewTransactionForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return NewTransactionForm(data=data)

    def test_new_transaction_valid_form(self):
        form = NewTransactionForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_signup_invalid_form_witch_blank_description(self):
        form = self.mixin_validate_form('', 'description')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_account(self):
        form = self.mixin_validate_form('', 'account')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_value(self):
        form = self.mixin_validate_form('', 'value')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_value_less_than_zero(self):
        form = self.mixin_validate_form('-1', 'value')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_value_equal_zero(self):
        form = self.mixin_validate_form('0', 'value')
        self.assertTrue(form.is_valid())
