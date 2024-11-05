"""Views for home page of the app."""

from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ..models import Account, Transaction, Transfer


class App(LoginRequiredMixin, View):
    """View for the home page of the app."""

    login_url = 'login'

    @staticmethod
    def get(request):
        """Return the home page of the app."""
        user = get_user_model().objects.get(email=request.user.email)
        accounts = Account.objects.filter(user=user)
        number_accounts = len(accounts)
        total_balance = sum(account.balance for account in accounts)

        all_bigger_transactions_of_month = list(
            Transaction.objects.filter(
                user=user,
                created_at__month=datetime.now().month,
            ).order_by('-value')
        )

        all_bigger_transfer_of_month = list(
            Transfer.objects.filter(
                user=user,
                created_at__month=datetime.now().month,
            ).order_by('-value')
        )

        all_bigger_transactions_of_month.extend(all_bigger_transfer_of_month)

        # Order by value and get the first 3
        all_bigger_transactions_of_month = sorted(
            all_bigger_transactions_of_month,
            key=lambda transaction: transaction.value,
            reverse=True,
        )[:3]

        monthly_expenses = sum(
            transaction.value
            for transaction in Transaction.objects.filter(
                user=user,
                created_at__month=datetime.now().month,
                type='EXPENSE',
            )
        )

        monthly_incomes = sum(
            transaction.value
            for transaction in Transaction.objects.filter(
                user=user,
                created_at__month=datetime.now().month,
                type='INCOME',
            )
        )

        bigger_transactions_of_month = []

        for transaction in all_bigger_transactions_of_month:
            if transaction.type == 'TRANSFER':
                account_name = f'{transaction.account_origin} -> {transaction.account_destination}'  # noqa
            else:
                account_name = transaction.account.name

            bigger_transactions_of_month.append({
                'type': transaction.type,
                'description': transaction.description,
                'value': transaction.value,
                'account': account_name,
            })

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
