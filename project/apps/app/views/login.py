from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from ..forms import LoginForm


def login_view(request):
    form = LoginForm()
    return render(
        request,
        'pages/app/login.html',
        context={'form': form, 'form_action': reverse('login_create')},
    )


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticate_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            login(request, authenticate_user)
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        messages.error(request, 'Error in data validation.')

    # Após o usuário se autenticar, redireciona ele para o app
    return redirect(reverse('app'))


@login_required(login_url='login')
def logout_view(request):
    if not request.POST:
        raise Http404()

    logout(request)
    messages.success(request, 'Logout completed successfully.')
    return redirect(reverse('login'))
