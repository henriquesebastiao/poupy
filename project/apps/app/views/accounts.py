from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from ..forms import AccountEditForm, DeleteAccountForm
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
        messages.success(request, 'Changes saved successfully.')

    return render(
        request,
        'pages/app/account_edit.html',
        context={
            'form': form,
        },
    )


@login_required(login_url='login')
def new_account(request):
    form = AccountEditForm()
    return render(
        request,
        'pages/app/new_account.html',
        context={
            'form': form,
        },
    )


@login_required(login_url='login')
def new_account_create(request):
    if not request.POST:
        raise Http404()

    form = AccountEditForm(request.POST)

    if form.is_valid():
        account = form.save(commit=False)
        account.name = request.POST['name'].strip().title()

        account = Account(
            name=account.name,
            user=request.user,
            balance=0.00,
        )

        account.save()
        messages.success(request, 'Account created successfully.')

    return redirect('accounts')


@login_required(login_url='login')
def delete_account(request):
    form = DeleteAccountForm()
    return render(
        request,
        'pages/app/delete_account.html',
        context={
            'form': form,
        },
    )


@login_required(login_url='login')
def delete_account_confirm(request):
    if not request.POST:
        raise Http404()

    form = DeleteAccountForm(request.POST)

    if form.is_valid():
        account = Account.objects.get(
            id=request.POST['account'],
            user=request.user,
        )

        if account.balance == 0:
            account.delete()
            messages.success(request, 'Account deleted successfully.')
        else:
            messages.error(
                request,
                'It is not possible to delete an account with a non-zero balance.',
            )

    return redirect('accounts')
