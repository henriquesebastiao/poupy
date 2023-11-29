from django import forms
from django.contrib.auth.models import User

from .models import Account, Transaction


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite sua senha novamente'}
        ),
        error_messages={'required': 'Você precisa repetir sua senha'},
        label='Repita sua senha',
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
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
            'email': 'Email',
        }

        # Ver isso melhor
        error_messages = {
            'email': {'required': 'Você precisa inserir um endereço de email'},
            'username': {
                'required': 'Você precisa inserir um nome de usuário'
            },
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Insira seu nome'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Insira seu sobrenome'}
            ),
            'username': forms.TextInput(
                attrs={'placeholder': 'Insira um nome de usuário'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Insira seu melhor email'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Insira uma senha segura'}
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(
            attrs={'placeholder': 'Insira seu nome de usuário'}
        ),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Insira sua senha'}),
    )


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'name',
            'balance',
        ]

        labels = {
            'name': 'Nome da conta',
            'balance': 'Saldo',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Insira o nome da conta'}
            ),
            'balance': forms.NumberInput(
                attrs={'placeholder': 'Insira o saldo da conta'}
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

        widgets = {
            'description': forms.TextInput(
                attrs={'placeholder': 'Insert the description of transaction'}
            )
        }


class NewExpenseForm(forms.ModelForm):
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
