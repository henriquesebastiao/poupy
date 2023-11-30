from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from ..forms import SignupForm


def signup(request):
    signup_form_data = request.session.get('signup_form_data', None)
    form = SignupForm(signup_form_data)
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
    form = SignupForm(post)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)  # Salva a senha criptografada no db
        user.save()
        messages.success(request, 'User created successfully.')

        del request.session['signup_form_data']
    else:
        messages.error(request, 'Invalid form, try again.')
        return redirect('signup')

    # Após o usuário ser criado ele já redirecionado para fazer login
    return redirect('login')
