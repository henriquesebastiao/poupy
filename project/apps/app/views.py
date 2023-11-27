from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm
from .models import Account, Transaction, User


def app(request):
    # Redireciona para a página de login caso o usuário tente acessar o app, mas não esteja logado
    if request.user.id is None:
        return redirect('login')

    user = User.objects.get(email=request.user.email)
    accounts = Account.objects.filter(user=user)
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
            'bigger_transactions_of_month': bigger_transactions_of_month,
            'monthly_expenses': monthly_expenses,
            'monthly_incomes': monthly_incomes,
        },
    )


def signup(request):
    signup_form_data = request.session.get('signup_form_data', None)
    form = RegisterForm(signup_form_data)
    return render(
        request,
        'pages/app/signup.html',
        context={
            'form': form,
        },
    )


def user_create(request):
    if not request.POST:
        raise Http404()
    post = request.POST
    request.session['signup_form_data'] = post
    form = RegisterForm(post)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)  # Salva a senha criptografada no db
        user.save()
        messages.success(request, 'Usuário criado com sucesso.')

        del request.session['signup_form_data']

    # Após o usuário ser criado ele já redirecionado para fazer login
    return redirect('login')


def auth(request):
    form = LoginForm()
    return render(
        request,
        'pages/app/login.html',
        context={'form': form, 'form_action': reverse('login_create')},
    )


def auth_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    app_url = reverse('app')

    if form.is_valid():
        authenticate_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            messages.success(request, 'Usuário logado com sucesso.')
            login(request, authenticate_user)
        else:
            messages.error(request, 'Credenciais inválidas.')
    else:
        messages.error(request, 'Erro na validação dos dados.')

    # Após o usuário se autenticar, redireciona ele para o app
    return redirect(app_url)


def transactions(request):
    user = User.objects.get(email='contato@henriquesebastiao.com')
    all_transactions = Transaction.objects.filter(user=user).order_by('-id')

    return render(
        request,
        'pages/app/transactions.html',
        context={
            'all_transactions': all_transactions,
        },
    )
