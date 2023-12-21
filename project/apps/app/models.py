"""Define the models for the app."""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonInfo(models.Model):
    """
    Abstract model for common fields in the models.
    This model is used to avoid repeating the same fields in the models.

    Attributes:
        user: The user that created the transaction.
        created_at: The date and time that the transaction was created.
        updated_at: The date and time that the transaction was updated.
    """

    class Meta:
        abstract = True

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_edited(self) -> bool:
        """Check if the transfer was edited."""
        if self.created_at.strftime(
            '%Y-%m-%d %H:%M'
        ) != self.updated_at.strftime('%Y-%m-%d %H:%M'):
            return True
        return False


class TransactionMixin(models.Model):
    """
    Abstract model for common fields in the transactions.

    Attributes:
        description: The description of the transaction.
        value: The value of the transaction.
    """

    class Meta:
        abstract = True

    description = models.CharField(max_length=255, null=False)
    value = models.DecimalField(decimal_places=2, null=False, max_digits=14)


class Account(CommonInfo):
    """Model for the Account."""

    name = models.CharField(max_length=55, null=False)
    balance = models.DecimalField(
        decimal_places=2, null=False, default=0.00, max_digits=14
    )

    def __str__(self):
        return self.name


class Transaction(CommonInfo, TransactionMixin):
    """Model for the Transaction."""

    class TransactionType(
        models.TextChoices
    ):  # pylint: disable=too-many-ancestors
        """Define the type of the transaction."""

        INCOME = 'INCOME', _('Receita')
        EXPENSE = 'EXPENSE', _('Despesa')
        TRANSFER = 'TRANSFER', _('Transferência')

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=8,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
        null=False,
    )

    def __str__(self):
        return self.description


class Transfer(CommonInfo, TransactionMixin):
    """Model for the Transfer."""

    account_origin = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account_origin'
    )
    account_destination = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='account_destination'
    )
    type = models.CharField(max_length=8, default='TRANSFER', null=False)

    def __str__(self):
        return self.description
