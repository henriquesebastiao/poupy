from django.urls import path

from .api.accounts import get_account, get_all_accounts

urlpatterns = [
    path('accounts/get-all/', get_all_accounts, name='get_all_accounts'),
    path('accounts/get/<int:id>/', get_account, name='get_account'),
]
