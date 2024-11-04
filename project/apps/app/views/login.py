"""Views for login page."""

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from ..forms import LoginForm


class LoginView(FormView):
    """View for login page."""

    template_name = 'pages/app/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = reverse('login_create')
        return context


class LoginCreateView(FormView):
    """View for login create."""

    template_name = 'pages/app/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        authenticate_user = authenticate(
            self.request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            login(self.request, authenticate_user)
            # Após o usuário se autenticar, redireciona ele para o app
            return redirect(reverse('app'))

        # If the user is not authenticated, an error message is displayed.
        messages.error(self.request, 'Invalid credentials.')
        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error in data validation.')
        return super().form_invalid(form)


class LoginDemoCreateView(FormView):
    """View for login demo user create."""

    template_name = 'pages/app/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        authenticate_user = authenticate(
            self.request,
            username='demo',
            password='dEmo@user1',
        )

        if authenticate_user is not None:
            login(self.request, authenticate_user)
            return redirect(reverse('app'))

        messages.error(self.request, 'Demo user invalid')
        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error in data validation.')
        return super().form_invalid(form)


@login_required(login_url='login')
def logout_view(request):
    """View for logout."""
    if not request.POST:
        raise Http404()

    logout(request)
    messages.success(request, 'Logout completed successfully.')
    return redirect(reverse('login'))
