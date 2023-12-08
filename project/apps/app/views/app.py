from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ..models import Account, Transaction, User


class App(LoginRequiredMixin, View):
    login_url = 'login'

    @staticmethod
    def get(request):
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
