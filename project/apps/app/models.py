"""Define the models for the app."""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    """Model for the Account."""

    name = models.CharField(max_length=55, null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    balance = models.DecimalField(
        decimal_places=2, null=False, default=0.00, max_digits=14
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Model for the Transaction."""

    class TransactionType(
        models.TextChoices
    ):  # pylint: disable=too-many-ancestors
        """Define the type of the transaction."""

        INCOME = 'INCOME', _('Receita')
        EXPENSE = 'EXPENSE', _('Despesa')
        TRANSFER = 'TRANSFER', _('Transferência')

    description = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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


class Transfer(models.Model):
    """Model for the Transfer."""

    description = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    account_origin = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account_origin'
    )
    account_destination = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account_destination'
    )
    value = models.DecimalField(decimal_places=2, null=False, max_digits=14)
    transaction_date = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=8, default='TRANSFER', null=False)

    def __str__(self):
        return self.description
