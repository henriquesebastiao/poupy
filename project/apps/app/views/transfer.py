from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from ..forms import TransferForm
from ..models import Account, Transaction


@login_required(login_url='login')
def new_transfer(request):
    form = TransferForm()
    return render(
        request,
        'pages/app/new_transfer.html',
        context={
            'form': form,
        },
    )


@login_required(login_url='login')
def new_transfer_create(request):
    if not request.POST:
        raise Http404()

    form = TransferForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        account_origin = Account.objects.get(name=data['account_origin'])
        account_destination = Account.objects.get(
            name=data['account_destination']
        )

        if account_origin.balance >= data['value']:
            transaction_origin = Transaction(
                description=data['description'],
                user=request.user,
                account=account_origin,
                value=data['value'],
                transaction_date=datetime.now(),
                type=Transaction.TransactionType.TRANSFER,
            )
            transaction_destination = Transaction(
                description=data['description'],
                user=request.user,
                account=account_destination,
                value=data['value'],
                transaction_date=datetime.now(),
                type=Transaction.TransactionType.TRANSFER,
            )

            transaction_origin.save()
            transaction_destination.save()

            account_origin.balance -= data['value']
            account_destination.balance += data['value']

            account_origin.save()
            account_destination.save()

            return redirect('app')

        else:
            messages.error(
                request, 'Saldo insuficiente para realizar a transferência.'
            )
            return redirect('new_transfer')
