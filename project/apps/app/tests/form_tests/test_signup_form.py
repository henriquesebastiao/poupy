from django.test import TestCase

from project.apps.app.forms import SignupForm


class SignupTestForm(TestCase):
    data = {
        'first_name': 'Test',
        'last_name': 'Test',
        'username': 'test',
        'email': 'test@email.com',
        'password': 'Test@1234',
        'repeat_password': 'Test@1234',
    }

    def mixin_validate_form(self, string_to_validate: str, *args: str) -> SignupForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return SignupForm(data=data)

    def test_signup_valid_form(self):
        form = SignupForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_signup_invalid_form_witch_weak_password(self):
        form = self.mixin_validate_form('test', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_blank_password(self):
        form = self.mixin_validate_form('', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_shorter_than_eight_characters(
        self,
    ):
        form = self.mixin_validate_form('A1@a', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_numbers(self):
        form = self.mixin_validate_form('Test@abc', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_uppercase_letters(
        self,
    ):
        form = self.mixin_validate_form('test@1234', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_lowercase_letters(
        self,
    ):
        form = self.mixin_validate_form('TEST@1234', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_password_without_special_characters(
        self,
    ):
        form = self.mixin_validate_form('Test1234', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_signup_valid_form_witch_first_name_blank(self):
        form = self.mixin_validate_form('', 'first_name')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_last_name_blank(self):
        form = self.mixin_validate_form('', 'last_name')
        self.assertTrue(form.is_valid())

    def test_signup_invalid_form_witch_username_blank(self):
        form = self.mixin_validate_form('', 'username')
        self.assertFalse(form.is_valid())

    def test_signup_invalid_form_witch_email_blank(self):
        form = self.mixin_validate_form('', 'email')
        self.assertFalse(form.is_valid())
