from datetime import datetime

from django.shortcuts import render

from .models import Account, Transaction, User


def app(request):
    user = User.objects.get(email='contato@henriquesebastiao.com')
    accounts = Account.objects.filter(user=user)
    total_balance = sum([account.balance for account in accounts])
    bigger_transactions_of_month = Transaction.objects.filter(
        user=user,
        transaction_date__month=datetime.now().month,
    ).order_by('-value')[:3]

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
        },
    )


def signup(request):
    return render(request, 'pages/app/signup.html')


def login(request):
    return render(request, 'pages/app/login.html')
