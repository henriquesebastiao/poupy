from unittest import TestCase

from ..forms import LoginForm


class LoginFormUnitTest(TestCase):
    def setUp(self):
        self.form = LoginForm()

    # Test placeholders
    def test_username_placeholder_is_correct(self):
        placeholder = self.form.fields['username'].widget.attrs['placeholder']
        self.assertEqual('Enter your username', placeholder)

    def test_password_placeholder_is_correct(self):
        placeholder = self.form.fields['password'].widget.attrs['placeholder']
        self.assertEqual('Enter your password', placeholder)

    # Test labels
    def test_username_label_is_correct(self):
        label = self.form.fields['username'].label
        self.assertEqual('Username', label)

    def test_password_label_is_correct(self):
        label = self.form.fields['password'].label
        self.assertEqual('Password', label)
