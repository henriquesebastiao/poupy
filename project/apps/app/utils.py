import re
from datetime import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.http import Http404

from .models import Account, Transaction


def add_transaction(request, form: ModelForm, transaction_type: str):
    """
    Add new transaction and update value in account

    Args:
        request: HttpRequest
        form: ModelForm of Transaction
        transaction_type: Type of transaction (expanse or income)
    """
    if not request.POST:
        raise Http404()

    if form.is_valid():
        # Add new expanse
        transaction = form.save(commit=False)
        transaction.transaction_date = datetime.now()
        transaction.user_id = request.user.id
        if transaction_type == 'income':
            transaction.type = Transaction.TransactionType.INCOME
        transaction.save()

        # Update value in account
        account = Account.objects.get(
            name=transaction.account.name, user=request.user
        )
        if transaction_type == 'expanse':
            account.balance -= transaction.value
        else:
            account.balance += transaction.value
        account.save()


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            (
                'Password must have at least one uppercase letter, '
                'one lowercase letter and one number. The length should be '
                'at least 8 characters.'
            ),
            code='invalid',
        )
