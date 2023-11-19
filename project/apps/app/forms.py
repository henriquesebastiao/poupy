from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
