from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from ..forms import TransactionsEditForm
from ..models import Transaction, User


class TransactionsView(LoginRequiredMixin, TemplateView):
    login_url = 'login'

    template_name = 'pages/app/transactions.html'

    def get_context_data(self, **kwargs):
        user = User.objects.get(email=self.request.user.email)
        all_transactions = Transaction.objects.filter(user=user).order_by(
            '-id'
        )

        context = super().get_context_data(**kwargs)
        context['all_transactions'] = all_transactions
        return context


class TransactionEditView(LoginRequiredMixin, UpdateView):
    login_url = 'login'

    model = Transaction
    form_class = TransactionsEditForm
    template_name = 'pages/app/transaction_edit.html'
    pk_url_kwarg = 'transaction_id'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, 'Changes saved successfully.')
        return reverse_lazy('transactions')
