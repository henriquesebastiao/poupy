from django.test import TestCase

from ..forms import SignupForm


class SignupFormUnitTest(TestCase):
    def setUp(self):
        self.form = SignupForm()

    # Test placeholders
    def test_first_name_placeholder_is_correct(self):
        placeholder = self.form.fields['first_name'].widget.attrs[
            'placeholder'
        ]
        self.assertEqual('Enter your first name', placeholder)

    def test_last_name_placeholder_is_correct(self):
        placeholder = self.form.fields['last_name'].widget.attrs['placeholder']
        self.assertEqual('Enter your last name', placeholder)

    def test_username_placeholder_is_correct(self):
        placeholder = self.form.fields['username'].widget.attrs['placeholder']
        self.assertEqual('Enter a username', placeholder)

    def test_email_placeholder_is_correct(self):
        placeholder = self.form.fields['email'].widget.attrs['placeholder']
        self.assertEqual('Enter your best email', placeholder)

    def test_password_placeholder_is_correct(self):
        placeholder = self.form.fields['password'].widget.attrs['placeholder']
        self.assertEqual('Enter a secure password', placeholder)

    # Test labels
    def test_first_name_label_is_correct(self):
        label = self.form.fields['first_name'].label
        self.assertEqual('First name', label)

    def test_last_name_label_is_correct(self):
        label = self.form.fields['last_name'].label
        self.assertEqual('Last name', label)

    def test_username_label_is_correct(self):
        label = self.form.fields['username'].label
        self.assertEqual('Username', label)

    def test_email_label_is_correct(self):
        label = self.form.fields['email'].label
        self.assertEqual('Email', label)
