"""Views for the Expanse app."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from ..forms import NewTransactionForm
from ..models import Account


class ExpanseView(LoginRequiredMixin, FormView):
    """View for the expanse page."""

    login_url = 'login'

    template_name = 'pages/app/new_expanse.html'
    form_class = NewTransactionForm

    def get_context_data(self, **kwargs):  # pylint: disable=useless-parent-delegation
        return super().get_context_data(**kwargs)


class ExpanseCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new expanse."""

    # pylint: disable=duplicate-code
    login_url = 'login'

    form_class = NewTransactionForm
    success_url = reverse_lazy('app')

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user_id = self.request.user.id

        account = Account.objects.get(name=transaction.account.name, user=self.request.user)
        account.balance -= transaction.value
        account.save()
        return super().form_valid(form)
