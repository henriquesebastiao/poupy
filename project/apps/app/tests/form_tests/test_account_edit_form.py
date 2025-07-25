from django.test import TestCase

from project.apps.app.forms import AccountEditForm


class AccountEditTestForm(TestCase):
    data = {
        'name': 'Bank',
        'balance': 100.00,
    }

    def mixin_validate_form(self, string_to_validate: str, *args: str) -> AccountEditForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return AccountEditForm(data=data)

    def test_account_edit_valid_form(self):
        form = AccountEditForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_account_edit_invalid_form_witch_blank_name(self):
        form = self.mixin_validate_form('', 'name')
        self.assertFalse(form.is_valid())

    def test_account_edit_invalid_form_witch_balance_less_than_zero(self):
        form = self.mixin_validate_form('-1', 'balance')
        self.assertFalse(form.is_valid())

    def test_account_edit_invalid_form_witch_balance_equal_zero(self):
        form = self.mixin_validate_form('0', 'balance')
        self.assertTrue(form.is_valid())
