from django.shortcuts import render

from .models import Account, User, Transaction


def app(request):
    user = User.objects.get(email='contato@henriquesebastiao.com')
    accounts = Account.objects.filter(user=user)
    total_balance = sum([account.balance for account in accounts])
    transactions = Transaction.objects.filter(user=user)

    return render(
        request,
        'pages/app/home.html',
        context={
            'logo_name_url': 'app',
            'user_first_name': user.first_name,
            'total_balance': total_balance,
            'accounts': accounts,
            'transactions': transactions,
        },
    )
