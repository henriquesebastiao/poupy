"""Define the forms used in the application."""

import re
from dataclasses import dataclass

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Account, Transaction


def strong_password(password):
    """
    Validates that the password is strong enough, if not, raises a ValidationError.

    Args:
        password: The password to be validated.
    """
    regex = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])(?=.*[a-zA-Z0-9@#$%^&+=!]).{8,}$'
    )

    if not regex.match(password):
        raise ValidationError(
            (
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.'
            ),
            code='invalid',
        )


class SignupForm(forms.ModelForm):
    """Form used to register a new user."""

    def __init__(self, *args, **kwargs):
        """To avoid having to overwrite the fields, I just define them as required"""
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        # Username and password are already required by default

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter a secure password'}
        ),
        label='Password',
        validators=[strong_password],
    )

    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password again'}
        ),
        error_messages={'required': 'You need to repeat your password'},
        label='Repeat your password',
    )

    @dataclass
    class Meta:
        """Meta class to define the model and the fields to be used."""

        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'Email',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter your first name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter your last name'}
            ),
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter a username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your best email'}
            ),
        }

    def clean_email(self):
        """Validates that the email is unique"""
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('This email is already in use.')
        return email

    def clean(self):
        """Validates that the password and repeat_password fields are equal"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise ValidationError(
                {
                    'repeat_password': 'Password and password repeat must be equal.'
                }
            )


class LoginForm(forms.Form):
    """Form used to authenticate a user."""

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        ),
    )


class AccountEditForm(forms.ModelForm):
    """Form used to edit an account."""

    @dataclass
    class Meta:
        """Meta class to define the model and the fields to be used."""

        model = Account
        fields = [
            'name',
            'balance',
        ]

        labels = {
            'name': 'Account name',
            'balance': 'Balance',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter account name'}
            ),
            'balance': forms.NumberInput(
                attrs={'placeholder': 'Enter account balance'}
            ),
        }


class TransactionsEditForm(forms.ModelForm):
    """Form used to edit a transaction."""

    @dataclass
    class Meta:
        """Meta class to define the model and the fields to be used."""

        model = Transaction
        fields = [
            'description',
            'account',
            'value',
            'type',
        ]

        labels = {
            'description': 'Description',
            'account': 'Account',
            'value': 'Value',
            'type': 'Type',
        }


class NewTransactionForm(forms.ModelForm):
    """Form used to create a new transaction."""

    @dataclass
    class Meta:
        """Meta class to define the model and the fields to be used."""

        model = Transaction
        fields = [
            'description',
            'account',
            'value',
        ]

        widgets = {
            'description': forms.TextInput(
                attrs={'placeholder': 'Insert the description of transaction'}
            ),
            'value': forms.NumberInput(
                attrs={'placeholder': 'Insert the value'}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['account'].queryset = Account.objects.filter(user=user)


class TransferForm(forms.Form):
    """Form used to transfer money between accounts."""

    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(
            attrs={'placeholder': 'Insert the description of transaction'}
        ),
    )

    account_origin = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        label='Source account',
        widget=forms.Select(),
    )

    account_destination = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        label='Target account',
        widget=forms.Select(),
    )

    value = forms.DecimalField(
        label='Value',
        widget=forms.NumberInput(
            attrs={'placeholder': 'Insert the value of transaction'}
        ),
    )

    def clean(self):
        """Validates that the account_origin and account_destination fields are not equal"""
        cleaned_data = super().clean()
        account_origin = cleaned_data.get('account_origin')
        account_destination = cleaned_data.get('account_destination')

        if account_origin == account_destination:
            raise ValidationError(
                {
                    'account_destination': 'Source account and target account must be different.'
                }
            )

        value = cleaned_data.get('value')

        if value is None or value <= 0:
            raise ValidationError(
                {'value': 'Value must be greater than zero.'}
            )


class DeleteAccountForm(forms.Form):
    """Form used to delete an account."""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['account'].queryset = Account.objects.filter(user=user)

    account = forms.ModelChoiceField(
        queryset=Account.objects.none(),
        label='Account',
        widget=forms.Select(),
    )


class UserApplicationEditForm(forms.ModelForm):
    """Form used to edit the user."""

    def __init__(self, *args, **kwargs):
        """To avoid having to overwrite the fields, I just define them as required"""
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['username'].required = True
        self.fields['email'].required = True

    @dataclass
    class Meta:
        """Meta class to define the model and the fields to be used."""

        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'Email',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter your first name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter your last name'}
            ),
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter a username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your best email'}
            ),
        }

    def clean_email(self):
        """Validates that the email is unique"""
        email = self.cleaned_data.get('email')

        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('This email is already in use.')
        return email

    def clean_username(self):
        """Validates that the username is unique"""
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            raise ValidationError('This username is already in use.')
        return username


class UserApplicationEditPasswordForm(forms.ModelForm):
    """Form used to edit the user password."""

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter the new password'}
        ),
        error_messages={'required': 'You need to enter a new password'},
        label='New password',
        validators=[strong_password],
    )

    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your new password again'}
        ),
        error_messages={'required': 'You need to repeat your new password'},
        label='Repeat your new password',
    )

    @dataclass
    class Meta:
        """Meta class to define the model and the fields to be used."""

        model = get_user_model()
        fields = [
            'password',
        ]

        labels = {
            'password': 'New password',
        }

        widgets = {
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Enter a new password'}
            ),
        }

    def clean(self):
        """Validates that the password and repeat_password fields are equal"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise ValidationError(
                {
                    'repeat_password': 'Password and password repeat must be equal.'
                }
            )
