"""Views for transfer app."""

from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView

from ..forms import TransferForm
from ..models import Account, Transfer


class TransferView(LoginRequiredMixin, FormView):
    """Transfer view page."""

    login_url = 'login'

    template_name = 'pages/app/new_transfer.html'
    form_class = TransferForm

    def get_context_data(
        self, **kwargs
    ):  # pylint: disable=useless-parent-delegation
        return super().get_context_data(**kwargs)


class TransferCreateView(LoginRequiredMixin, FormView):
    """Transfer create view."""

    login_url = 'login'

    template_name = 'pages/app/new_transfer.html'
    form_class = TransferForm

    def form_valid(self, form):
        data = form.cleaned_data
        account_origin = Account.objects.get(name=data['account_origin'])
        account_destination = Account.objects.get(
            name=data['account_destination']
        )

        if account_origin.balance >= data['value']:
            transaction = Transfer(
                description=data['description'],
                user=self.request.user,
                account_origin=account_origin,
                account_destination=account_destination,
                value=data['value'],
                transaction_date=datetime.now(),
            )

            account_origin.balance -= data['value']
            account_destination.balance += data['value']

            account_origin.save()
            account_destination.save()

            transaction.save()

            return redirect('app')

        # If the user does not have enough balance to make the transfer,
        # an error message is displayed.
        messages.error(
            self.request, 'Insufficient balance to make the transfer.'
        )
        return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error in data validation.')
        return super().form_invalid(form)
