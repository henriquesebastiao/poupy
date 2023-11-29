from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from ..forms import RegisterForm


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
