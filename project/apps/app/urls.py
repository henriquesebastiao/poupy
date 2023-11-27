from django.urls import path

from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('signup/', views.signup, name='signup'),
    path('user-create/', views.user_create, name='user_create'),
    path('login/', views.auth, name='login'),
    path('login/create/', views.auth_create, name='login_create'),
    path('transactions/', views.transactions, name='transactions'),
]
