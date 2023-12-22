from django.contrib.auth.models import User
from django.test import TestCase

from project.apps.app.forms import TransferForm
from project.apps.app.models import Account


class TransferTestForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
        )
        self.account_origin = Account.objects.create(
            name='Test Account Origin',
            balance=1000.00,
            user=self.user,
        )
        self.account_destination = Account.objects.create(
            name='Test Account Destination',
            balance=1000.00,
            user=self.user,
        )
        self.data = {
            'description': 'Test Transfer',
            'account_origin': self.account_origin.id,
            'account_destination': self.account_destination.id,
            'value': 100.00,
        }

    def mixin_validate_form(
        self, string_to_validate: str, *args: str
    ) -> TransferForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return TransferForm(data=data)

    def test_new_transfer_valid_form(self):
        form = TransferForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_signup_invalid_form_witch_blank_description(self):
        form = self.mixin_validate_form('', 'description')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_account_origin(self):
        form = self.mixin_validate_form('', 'account_origin')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_account_destination(self):
        form = self.mixin_validate_form('', 'account_destination')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_value(self):
        form = self.mixin_validate_form('', 'value')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_value_less_than_zero(self):
        form = self.mixin_validate_form('-1', 'value')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_value_equal_zero(self):
        form = self.mixin_validate_form('0', 'value')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_account_origin_equal_account_destination(
        self,
    ):
        form = self.mixin_validate_form(
            self.account_origin.id, 'account_destination'
        )
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_account_destination_equal_account_origin(
        self,
    ):
        form = self.mixin_validate_form(
            self.account_destination.id, 'account_origin'
        )
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_account_origin_not_exists(self):
        form = self.mixin_validate_form('999999', 'account_origin')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_account_destination_not_exists(self):
        form = self.mixin_validate_form('999999', 'account_destination')
        self.assertFalse(form.is_valid())
