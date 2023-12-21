from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from ..forms import UserApplicationEditForm, UserApplicationEditPasswordForm


class UserApplicationUpdateView(LoginRequiredMixin, View):
    login_url = 'login'

    @staticmethod
    def get(request, *args, **kwargs):
        """
        Load the form with the current logged-in
        user data on the screen so that they can be edited
        """
        form = UserApplicationEditForm(
            data=request.POST or None, instance=request.user
        )

        return render(
            request,
            'pages/app/settings.html',
            context={
                'form': form,
            },
        )

    @staticmethod
    def post(request, *args, **kwargs):
        """
        Update the user's data with the data
        entered in the form

        Returns:
            Redirect to app page
        """
        form = UserApplicationEditForm(
            data=request.POST or None, instance=request.user
        )

        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST['first_name'].strip().title()
            user.last_name = request.POST['last_name'].strip().title()
            user.username = request.POST['username'].strip()
            user.email = request.POST['email'].strip()
            user.save()

        return redirect('app')


class UserApplicationUpdatePasswordView(LoginRequiredMixin, View):
    login_url = 'login'

    @staticmethod
    def get(request, *args, **kwargs):
        form = UserApplicationEditPasswordForm

        return render(
            request,
            'pages/app/new_password.html',
            context={
                'form': form,
            },
        )

    @staticmethod
    def post(request, *args, **kwargs):
        form = UserApplicationEditPasswordForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            request.user.set_password(request.POST['password'].strip())
            request.user.save()
            logout(request)
            messages.success(
                request, 'Password changed successfully. Please login again.'
            )

            return redirect('login')
