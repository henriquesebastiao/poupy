from unittest import TestCase

from ..forms import TransferForm


class TransferFormUnitTest(TestCase):
    def setUp(self):
        self.form = TransferForm()

    # Test placeholders
    def test_description_placeholder_is_correct(self):
        placeholder = self.form.fields['description'].widget.attrs[
            'placeholder'
        ]
        self.assertEqual('Insert the description of transaction', placeholder)

    def test_value_placeholder_is_correct(self):
        placeholder = self.form.fields['value'].widget.attrs['placeholder']
        self.assertEqual('Insert the value of transaction', placeholder)

    # Test labels
    def test_description_label_is_correct(self):
        label = self.form.fields['description'].label
        self.assertEqual('Description', label)

    def test_account_origin_label_is_correct(self):
        label = self.form.fields['account_origin'].label
        self.assertEqual('Source account', label)

    def test_account_destination_label_is_correct(self):
        label = self.form.fields['account_destination'].label
        self.assertEqual('Target account', label)

    def test_value_label_is_correct(self):
        label = self.form.fields['value'].label
        self.assertEqual('Value', label)
