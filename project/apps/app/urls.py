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
]
