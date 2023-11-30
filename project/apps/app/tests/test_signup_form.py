from unittest import TestCase

from django.test import TestCase as DjangoTesteCase
from django.urls import reverse

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


class SignupFormIntegrationTeste(DjangoTesteCase):
    def setUp(self):
        self.form_data = {
            'username': 'user',
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'test@email.com',
            'password': '1234abCD@',
            'repeat_password': '1234abCD@',
        }
        return super().setUp()

    def test_field_username_cannot_be_empty(self):
        """Test if the form is invalid when the field username is empty."""
        self.form_data['username'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )

    def test_field_first_name_cannot_be_empty(self):
        """Test if the form is invalid when the field first_name is empty."""
        self.form_data['first_name'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )

    def test_field_last_name_cannot_be_empty(self):
        """Test that the form is not invalid even if the last_name field is empty."""
        self.form_data['last_name'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertNotIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )

    def test_field_email_cannot_be_empty(self):
        """Test if the form is invalid when the field email is empty."""
        self.form_data['email'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )

    def test_field_password_cannot_be_empty(self):
        """Test if the form is invalid when the field password is empty."""
        self.form_data['password'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )

    def test_field_repeat_password_cannot_be_empty(self):
        """Test if the form is invalid when the field repeat_password is empty."""
        self.form_data['repeat_password'] = ''
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )

    def test_field_password_not_accept_weak_password(self):
        """Test if the form is invalid when the field password is weak."""
        self.form_data['password'] = 'abc'
        response = self.client.post(
            reverse('user_create'), data=self.form_data, follow=True
        )
        self.assertIn(
            'Invalid form, try again.', response.content.decode('utf-8')
        )
