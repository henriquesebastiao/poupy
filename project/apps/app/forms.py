from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite sua senha novamente'}
        ),
        error_messages={'required': 'Voê precisa repetir sua senha'},
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


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
