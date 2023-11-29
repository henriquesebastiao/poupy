from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..forms import AccountEditForm
from ..models import Account, User


@login_required(login_url='login')
def accounts_view(request):
    user = User.objects.get(email=request.user.email)
    accounts = Account.objects.filter(user=user)
    return render(
        request,
        'pages/app/accounts.html',
        context={
            'accounts': accounts,
        },
    )


@login_required(login_url='login')
def account_edit(request, account_id):
    account = Account.objects.get(id=account_id, user=request.user)

    form = AccountEditForm(data=request.POST or None, instance=account)

    if form.is_valid():
        account = form.save(commit=False)
        # Format the name account for title and remove blank spaces the sides
        account.name = request.POST['name'].strip().title()
        account.save()
        messages.success(request, 'Alterações salvas com sucesso.')

    return render(
        request,
        'pages/app/account_edit.html',
        context={
            'form': form,
        },
    )
