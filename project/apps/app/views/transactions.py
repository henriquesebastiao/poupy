from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..forms import TransactionsEditForm
from ..models import Transaction, User


@login_required(login_url='login')
def transactions(request):
    user = User.objects.get(email='contato@henriquesebastiao.com')
    all_transactions = Transaction.objects.filter(user=user).order_by('-id')

    return render(
        request,
        'pages/app/transactions.html',
        context={
            'all_transactions': all_transactions,
        },
    )


@login_required(login_url='login')
def transaction_edit(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id, user=request.user)
    form = TransactionsEditForm(
        data=request.POST or None, instance=transaction
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Alterações salvas com sucesso.')

    return render(
        request, 'pages/app/transaction_edit.html', context={'form': form}
    )
