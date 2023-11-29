from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import NewTransactionForm
from ..utils import add_transaction


@login_required(login_url='login')
def new_income(request):
    form = NewTransactionForm()
    return render(
        request,
        'pages/app/new_income.html',
        context={
            'form': form,
        },
    )


@login_required(login_url='login')
def new_income_create(request):
    add_transaction(request, NewTransactionForm(request.POST), 'income')
    return redirect('app')
