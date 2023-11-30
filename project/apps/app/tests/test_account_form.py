from django.test import TestCase

from ..forms import AccountEditForm, DeleteAccountForm


class AccountFormUnitTest(TestCase):
    def setUp(self):
        self.form = AccountEditForm

    # Test placeholders
    def test_name_placeholder_is_correct(self):
        placeholder = self.form.base_fields['name'].widget.attrs['placeholder']
        self.assertEqual('Enter account name', placeholder)

    def test_balance_placeholder_is_correct(self):
        placeholder = self.form.base_fields['balance'].widget.attrs[
            'placeholder'
        ]
        self.assertEqual('Enter account balance', placeholder)

    # Test labels
    def test_if_name_label_is_correct(self):
        label = self.form.base_fields['name'].label
        self.assertEqual('Account name', label)

    def test_balance_label_is_correct(self):
        label = self.form.base_fields['balance'].label
        self.assertEqual('Balance', label)


class DeleteAccountFormUnitTest(TestCase):
    # Test label
    def test_account_label_is_correct(self):
        form = DeleteAccountForm()
        label = form.fields['account'].label
        self.assertEqual('Account', label)
