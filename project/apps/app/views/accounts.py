"""Views for the accounts app."""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, ListView, UpdateView

from ..forms import AccountEditForm, DeleteAccountForm
from ..models import Account


class AccountListView(
    LoginRequiredMixin, ListView
):  # pylint: disable=too-many-ancestors
    """List all accounts."""

    login_url = 'login'

    template_name = 'pages/app/accounts.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).only(
            'id', 'name', 'balance'
        )


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """Update an account."""

    login_url = 'login'

    model = Account
    form_class = AccountEditForm
    template_name = 'pages/app/account_edit.html'
    success_url = reverse_lazy('accounts')
    pk_url_kwarg = 'account_id'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).only(
            'name', 'balance'
        )


class AccountCreateView(LoginRequiredMixin, CreateView):
    """Create a new account."""

    login_url = 'login'

    model = Account
    form_class = AccountEditForm
    template_name = 'pages/app/new_account.html'
    success_url = reverse_lazy('accounts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteAccountView(LoginRequiredMixin, FormView):
    """View to delete an account."""

    login_url = 'login'

    template_name = 'pages/app/delete_account.html'
    form_class = DeleteAccountForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(
        self, **kwargs
    ):  # pylint: disable=useless-parent-delegation
        return super().get_context_data(**kwargs)


class DeleteAccountConfirmView(LoginRequiredMixin, View):
    """View to confirm the deletion of an account."""

    login_url = 'login'

    @staticmethod
    def post(request):
        """Delete the account if request is POST."""

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
