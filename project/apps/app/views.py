from datetime import datetime

from django.shortcuts import render

from .forms import LoginForm, RegisterForm
from .models import Account, Transaction, User


def app(request):
    user = User.objects.get(email='contato@henriquesebastiao.com')
    accounts = Account.objects.filter(user=user)
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
            'bigger_transactions_of_month': bigger_transactions_of_month,
            'monthly_expenses': monthly_expenses,
            'monthly_incomes': monthly_incomes,
        },
    )


def signup(request):
    form = RegisterForm()
    return render(
        request,
        'pages/app/signup.html',
        context={
            'form': form,
        },
    )


def login(request):
    form = LoginForm()
    return render(
        request,
        'pages/app/login.html',
        context={
            'form': form,
        },
    )


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
