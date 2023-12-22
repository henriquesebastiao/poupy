from django.contrib.auth.models import User
from django.test import TestCase

from project.apps.app.forms import UserApplicationEditForm


class UserApplicationEditTestForm(TestCase):
    data = {
        'first_name': 'New First',
        'last_name': 'New Last',
        'username': 'new_username',
        'email': 'new@email.com',
    }

    def mixin_validate_form(
        self, string_to_validate: str, *args: str
    ) -> UserApplicationEditForm:
        data = self.data.copy()

        for field in args:
            data[field] = string_to_validate

        return UserApplicationEditForm(data=data)

    def test_user_application_edit_valid_form(self):
        form = UserApplicationEditForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_user_application_edit_invalid_form_witch_blank_first_name(self):
        form = self.mixin_validate_form('', 'first_name')
        self.assertFalse(form.is_valid())

    def test_user_application_edit_invalid_form_witch_blank_last_name(self):
        form = self.mixin_validate_form('', 'last_name')
        self.assertTrue(form.is_valid())

    def test_user_application_edit_invalid_form_witch_blank_username(self):
        form = self.mixin_validate_form('', 'username')
        self.assertFalse(form.is_valid())

    def test_user_application_edit_invalid_form_witch_blank_email(self):
        form = self.mixin_validate_form('', 'email')
        self.assertFalse(form.is_valid())

    def test_user_application_edit_invalid_form_witch_invalid_email(self):
        form = self.mixin_validate_form('test', 'email')
        self.assertFalse(form.is_valid())

    def test_user_application_edit_invalid_form_witch_email_already_exists(
        self,
    ):
        User.objects.create_user(
            username='test_other',
            password='Test@1234',
            email='other@email.com',
        )
        form = self.mixin_validate_form('other@email.com', 'email')
        self.assertFalse(form.is_valid())

    def test_user_application_edit_invalid_form_witch_username_already_exists(
        self,
    ):
        User.objects.create_user(
            username='test_other',
            password='Test@1234',
        )
        form = self.mixin_validate_form('test_other', 'username')
        self.assertFalse(form.is_valid())
