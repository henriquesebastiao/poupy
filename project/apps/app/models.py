from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    first_name = models.CharField(max_length=55, null=False)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Account(models.Model):
    name = models.CharField(max_length=55, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(
        decimal_places=2, null=False, default=0.00, max_digits=14
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = 'INCOME', _('Receita')
        EXPENSE = 'EXPENSE', _('Despesa')
        TRANSFER = 'TRANSFER', _('Transferência')

    description = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, null=False, max_digits=14)
    transaction_date = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(
        max_length=8,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
        null=False,
    )

    def __str__(self):
        return self.description
