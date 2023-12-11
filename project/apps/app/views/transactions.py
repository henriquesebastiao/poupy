"""Views for transactions."""

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView

from ..forms import TransactionsEditForm
from ..models import Account, Transaction, Transfer


class TransactionsView(LoginRequiredMixin, TemplateView):
    """Transactions view page."""

    login_url = 'login'

    template_name = 'pages/app/transactions.html'

    def get_context_data(self, **kwargs):
        user = get_user_model().objects.get(email=self.request.user.email)
        all_transactions = list(
            Transaction.objects.filter(user=user).order_by('-id')
        )

        all_transfers = list(
            Transfer.objects.filter(user=user).order_by('-id')
        )

        # Combine transfers and transactions so that they are displayed on the transactions page
        all_transactions.extend(all_transfers)

        context = super().get_context_data(**kwargs)
        context['all_transactions'] = all_transactions
        return context


class TransactionEditView(LoginRequiredMixin, UpdateView):
    """Transaction edit view page."""

    login_url = 'login'

    model = Transaction
    form_class = TransactionsEditForm
    template_name = 'pages/app/transaction_edit.html'
    pk_url_kwarg = 'transaction_id'

    def get_queryset(self):
        # If there is no transaction with this id, it means it is a transfer
        try:
            transaction = Transaction.objects.get(
                user=self.request.user,
            )
        except Transaction.DoesNotExist:
            transaction = Transfer.objects.filter(
                user=self.request.user,
                id=self.kwargs['transaction_id'],
            )
        return transaction

    def get_success_url(self):
        messages.success(self.request, 'Changes saved successfully.')
        return reverse_lazy('transactions')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Template information if the transaction is a transfer,
        # in which case the delete button for this transaction will not be displayed.
        context['transfer'] = self.object.type

        return context


class TransactionDeleteView(LoginRequiredMixin, View):
    """Transaction delete view."""

    login_url = 'login'

    @staticmethod
    def post(request, transaction_id, *args, **kwargs):
        """Delete transaction if request method is POST."""
        transaction = Transaction.objects.get(id=transaction_id)

        account = Account.objects.get(id=transaction.account.id)

        if transaction.type == 'INCOME':
            account.balance -= transaction.value
        elif transaction.type == 'EXPANSE':
            account.balance += transaction.value

        # In the future, we will implement the logic for deleting a transfer,
        # for now the delete button is not displayed when editing a transfer.

        account.save()
        transaction.delete()

        messages.success(request, 'Transaction deleted successfully.')

        return redirect('transactions')
