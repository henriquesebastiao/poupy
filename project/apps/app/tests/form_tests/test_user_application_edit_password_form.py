from django.test import TestCase

from project.apps.app.forms import UserApplicationEditPasswordForm


class UserApplicationPasswordEditTestForm(TestCase):
    data = {
        'password': 'Test@1234',
        'repeat_password': 'Test@1234',
    }

    def mixin_validate_form(
        self, string_to_validate: str, *args: str
    ) -> UserApplicationEditPasswordForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return UserApplicationEditPasswordForm(data=data)

    def test_user_application_password_edit_valid_form(self):
        form = UserApplicationEditPasswordForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_blank_password(
        self,
    ):
        form = self.mixin_validate_form('', 'password')
        self.assertFalse(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_blank_repeat_password(
        self,
    ):
        form = self.mixin_validate_form('', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_password_shorter_than_eight_characters(
        self,
    ):
        form = self.mixin_validate_form('A1@a', 'password', 'repeat_password')
        self.assertFalse(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_password_without_numbers(
        self,
    ):
        form = self.mixin_validate_form(
            'Test@abc', 'password', 'repeat_password'
        )
        self.assertFalse(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_password_without_uppercase_letters(
        self,
    ):
        form = self.mixin_validate_form(
            'test@1234', 'password', 'repeat_password'
        )
        self.assertFalse(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_password_without_lowercase_letters(
        self,
    ):
        form = self.mixin_validate_form(
            'TEST@1234', 'password', 'repeat_password'
        )
        self.assertFalse(form.is_valid())

    def test_user_application_password_edit_invalid_form_witch_passwords_without_special_characters(
        self,
    ):
        form = self.mixin_validate_form(
            'Test1234', 'password', 'repeat_password'
        )
        self.assertFalse(form.is_valid())
