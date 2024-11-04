"""URLs module."""

from django.urls import path

from ..app.views.accounts import (
    AccountCreateView,
    AccountListView,
    AccountUpdateView,
    DeleteAccountConfirmView,
    DeleteAccountView,
)
from ..app.views.app import App
from ..app.views.expanse import ExpanseCreateView, ExpanseView
from ..app.views.income import IncomeCreateView, IncomeView
from ..app.views.login import (
    LoginCreateView,
    LoginDemoCreateView,
    LoginView,
    logout_view,
)
from ..app.views.settings import (
    UserApplicationUpdatePasswordView,
    UserApplicationUpdateView,
)
from ..app.views.signup import SignupView, UserCreateView
from ..app.views.transactions import (
    TransactionDeleteView,
    TransactionEditView,
    TransactionsView,
)
from ..app.views.transfer import TransferCreateView, TransferView

urlpatterns = [
    path('', App.as_view(), name='app'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('user-create/', UserCreateView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/create/', LoginCreateView.as_view(), name='login_create'),
    path(
        'login/create-demo-user/',
        LoginDemoCreateView.as_view(),
        name='login_create_user_demo',
    ),
    path('logout/', logout_view, name='logout'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),
    path(
        'transaction/<int:transaction_id>/edit/',
        TransactionEditView.as_view(),
        name='transaction_edit',
    ),
    path(
        'transaction/<int:transaction_id>/delete/',
        TransactionDeleteView.as_view(),
        name='transaction_delete',
    ),
    path('accounts/', AccountListView.as_view(), name='accounts'),
    path(
        'accounts/new-account/',
        AccountCreateView.as_view(),
        name='new_account',
    ),
    path(
        'account/<int:account_id>/edit/',
        AccountUpdateView.as_view(),
        name='account_edit',
    ),
    path(
        'accounts/delete-account/',
        DeleteAccountView.as_view(),
        name='delete_account',
    ),
    path(
        'accounts/delete-account/confirm/',
        DeleteAccountConfirmView.as_view(),
        name='delete_account_confirm',
    ),
    path('new-expanse/', ExpanseView.as_view(), name='new_expanse'),
    path(
        'new-expanse/create/',
        ExpanseCreateView.as_view(),
        name='new_expanse_create',
    ),
    path('new-income/', IncomeView.as_view(), name='new_income'),
    path(
        'new-income/create/',
        IncomeCreateView.as_view(),
        name='new_income_create',
    ),
    path('new-transfer/', TransferView.as_view(), name='new_transfer'),
    path(
        'new-transfer/create/',
        TransferCreateView.as_view(),
        name='new_transfer_create',
    ),
    path('settings/', UserApplicationUpdateView.as_view(), name='settings'),
    path(
        'settings/new-password/',
        UserApplicationUpdatePasswordView.as_view(),
        name='new_password',
    ),
]
