from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('signup/', views.signup, name='signup'),
    path('user-create/', views.user_create, name='user_create'),
    path('login/', views.login, name='login'),
    path('transactions/', views.transactions, name='transactions'),
]
