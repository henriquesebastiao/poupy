from django.urls import path

from ..app.views.accounts import (
    account_edit,
    accounts_view,
    delete_account,
    delete_account_confirm,
    new_account,
    new_account_create,
)
from ..app.views.app import app
from ..app.views.expanse import new_expanse, new_expanse_create
from ..app.views.income import new_income, new_income_create
from ..app.views.login import login_create, login_view, logout_view
from ..app.views.signup import signup, user_create
from ..app.views.transactions import transaction_edit, transactions
from ..app.views.transfer import new_transfer, new_transfer_create

urlpatterns = [
    path('', app, name='app'),
    path('signup/', signup, name='signup'),
    path('user-create/', user_create, name='user_create'),
    path('login/', login_view, name='login'),
    path('login/create/', login_create, name='login_create'),
    path('logout/', logout_view, name='logout'),
    path('transactions/', transactions, name='transactions'),
    path(
        'transaction/<int:transaction_id>/edit/',
        transaction_edit,
        name='transaction_edit',
    ),
    path('accounts/', accounts_view, name='accounts'),
    path('accounts/new-account/', new_account, name='new_account'),
    path(
        'accounts/new-account/create/',
        new_account_create,
        name='new_account_create',
    ),
    path(
        'account/<int:account_id>/edit/',
        account_edit,
        name='account_edit',
    ),
    path('accounts/delete-account/', delete_account, name='delete_account'),
    path(
        'accounts/delete-account/confirm/',
        delete_account_confirm,
        name='delete_account_confirm',
    ),
    path('new-expanse/', new_expanse, name='new_expanse'),
    path(
        'new-expanse/create/',
        new_expanse_create,
        name='new_expanse_create',
    ),
    path('new-income/', new_income, name='new_income'),
    path('new-income/create/', new_income_create, name='new_income_create'),
    path('new-transfer/', new_transfer, name='new_transfer'),
    path(
        'new-transfer/create/',
        new_transfer_create,
        name='new_transfer_create',
    ),
]
