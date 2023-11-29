from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import (
    AccountEditForm,
    LoginForm,
    NewTransactionForm,
    RegisterForm,
    TransactionsEditForm,
    TransferForm,
)
from .models import Account, Transaction, User
from .utils import add_transaction


@login_required(login_url='login')
def app(request):
    user = User.objects.get(email=request.user.email)
    accounts = Account.objects.filter(user=user)
    number_accounts = len(accounts)
    total_balance = sum([account.balance for account in accounts])

    bigger_transactions_of_month = Transaction.objects.filter(
        user=user,
        transaction_date__month=datetime.now().month,
    ).order_by('-value')[:3]

    monthly_expenses = sum(
        [
            transaction.value
            for transaction in Transaction.objects.filter(
                user=user,
                transaction_date__month=datetime.now().month,
                type='EXPENSE',
            )
        ]
    )

    monthly_incomes = sum(
        [
            transaction.value
            for transaction in Transaction.objects.filter(
                user=user,
                transaction_date__month=datetime.now().month,
                type='INCOME',
            )
        ]
    )

    bigger_transactions_of_month = [
        {
            'type': transaction.type,
            'description': transaction.description,
            'value': transaction.value,
            'account': transaction.account.name,
        }
        for transaction in bigger_transactions_of_month
    ]

    return render(
        request,
        'pages/app/home.html',
        context={
            'logo_name_url': 'app',
            'user_first_name': user.first_name,
            'total_balance': total_balance,
            'accounts': accounts,
            'number_accounts': number_accounts,
            'bigger_transactions_of_month': bigger_transactions_of_month,
            'monthly_expenses': monthly_expenses,
            'monthly_incomes': monthly_incomes,
        },
    )


def signup(request):
    signup_form_data = request.session.get('signup_form_data', None)
    form = RegisterForm(signup_form_data)
    return render(
        request,
        'pages/app/signup.html',
        context={
            'form': form,
        },
    )


def user_create(request):
    if not request.POST:
        raise Http404()
    post = request.POST
    request.session['signup_form_data'] = post
    form = RegisterForm(post)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)  # Salva a senha criptografada no db
        user.save()
        messages.success(request, 'Usuário criado com sucesso.')

        del request.session['signup_form_data']

    # Após o usuário ser criado ele já redirecionado para fazer login
    return redirect('login')


def login_view(request):
    form = LoginForm()
    return render(
        request,
        'pages/app/login.html',
        context={'form': form, 'form_action': reverse('login_create')},
    )


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticate_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            login(request, authenticate_user)
        else:
            messages.error(request, 'Credenciais inválidas.')
    else:
        messages.error(request, 'Erro na validação dos dados.')

    # Após o usuário se autenticar, redireciona ele para o app
    return redirect(reverse('app'))


@login_required(login_url='login')
def logout_view(request):
    if not request.POST:
        raise Http404()

    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect(reverse('login'))


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


@login_required(login_url='login')
def new_expanse(request):
    form = NewTransactionForm()
    return render(
        request,
        'pages/app/new_expanse.html',
        context={
            'form': form,
        },
    )


@login_required(login_url='login')
def new_expanse_create(request):
    add_transaction(request, NewTransactionForm(request.POST), 'expanse')
    return redirect('app')


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
