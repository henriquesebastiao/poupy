from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('signup/', views.signup, name='signup'),
    path('user-create/', views.user_create, name='user_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('transactions/', views.transactions, name='transactions'),
    path(
        'transaction/<int:transaction_id>/edit/',
        views.transaction_edit,
        name='transaction_edit',
    ),
    path('accounts/', views.accounts_view, name='accounts'),
    path(
        'account/<int:account_id>/edit/',
        views.account_edit,
        name='account_edit',
    ),
    path('new-expanse/', views.new_expanse, name='new_expanse'),
    path(
        'new-expanse/create/',
        views.new_expanse_create,
        name='new_expanse_create',
    ),
    path('new-income/', views.new_income, name='new_income'),
    path(
        'new-income/create/', views.new_income_create, name='new_income_create'
    ),
    path('new-transfer/', views.new_transfer, name='new_transfer'),
    path(
        'new-transfer/create/',
        views.new_transfer_create,
        name='new_transfer_create',
    ),
]
