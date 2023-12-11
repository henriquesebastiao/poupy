"""Views for signup."""

from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView

from ..forms import SignupForm


class SignupView(FormView):
    """Signup view page."""

    template_name = 'pages/app/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.request.session['signup_form_data'] = form.cleaned_data
        return super().form_valid(form)


class UserCreateView(CreateView):
    """Create user view."""

    template_name = 'pages/app/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        raise Http404

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)  # Salva a senha criptografada no db
        user.save()
        messages.success(self.request, 'User created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid form, try again.')
        return super().form_invalid(form)
