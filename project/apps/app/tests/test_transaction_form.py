from unittest import TestCase

from ..forms import NewTransactionForm, TransactionsEditForm


class TransactionFormUnitTest(TestCase):
    def setUp(self):
        self.form = TransactionsEditForm()

    # Test labels
    def test_description_label_is_correct(self):
        label = self.form.fields['description'].label
        self.assertEqual('Description', label)

    def test_account_label_is_correct(self):
        label = self.form.fields['account'].label
        self.assertEqual('Account', label)

    def test_value_label_is_correct(self):
        label = self.form.fields['value'].label
        self.assertEqual('Value', label)

    def test_type_label_is_correct(self):
        label = self.form.fields['type'].label
        self.assertEqual('Type', label)


class NewTransactionFormUnitTest(TestCase):
    def setUp(self):
        self.form = NewTransactionForm()

    # Test placeholders
    def test_description_placeholder_is_correct(self):
        placeholder = self.form.fields['description'].widget.attrs[
            'placeholder'
        ]
        self.assertEqual('Insert the description of transaction', placeholder)

    def test_value_placeholder_is_correct(self):
        placeholder = self.form.fields['value'].widget.attrs['placeholder']
        self.assertEqual('Insert the value', placeholder)

    # Test labels
    def test_description_label_is_correct(self):
        label = self.form.fields['description'].label
        self.assertEqual('Description', label)

    def test_account_label_is_correct(self):
        label = self.form.fields['account'].label
        self.assertEqual('Account', label)

    def test_value_label_is_correct(self):
        label = self.form.fields['value'].label
        self.assertEqual('Value', label)
