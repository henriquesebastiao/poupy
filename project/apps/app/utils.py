from datetime import datetime

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
        account = Account.objects.get(name=transaction.account.name)
        if transaction_type == 'expanse':
            account.balance -= transaction.value
        else:
            account.balance += transaction.value
        account.save()
