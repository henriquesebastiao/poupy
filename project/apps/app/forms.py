from django import forms
from django.contrib.auth.models import User

from .models import Account, Transaction


class SignupForm(forms.ModelForm):
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password again'}
        ),
        error_messages={'required': 'You need to repeat your password'},
        label='Repeat your password',
    )

    class Meta:
        model = User
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
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Enter a secure password'}
            ),
        }


class LoginForm(forms.Form):
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
    class Meta:
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
    class Meta:
        model = Transaction
        fields = [
            'description',
            'account',
            'value',
            'transaction_date',
            'type',
        ]

        labels = {
            'description': 'Description',
            'account': 'Account',
            'value': 'Value',
            'transaction_date': 'Transaction date',
            'type': 'Type',
        }


class NewTransactionForm(forms.ModelForm):
    class Meta:
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
        super(NewTransactionForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['account'].queryset = Account.objects.filter(user=user)


class TransferForm(forms.Form):
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


class DeleteAccountForm(forms.Form):
    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        label='Account',
        widget=forms.Select(),
    )
