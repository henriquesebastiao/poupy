from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=55, null=False)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Account(models.Model):
    name = models.CharField(max_length=55, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(
        decimal_places=2, null=False, default=0.00, max_digits=14
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Expanse(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(decimal_places=2, null=False, max_digits=14)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Income(models.Model):
    description = models.CharField(max_length=255)
    value = models.DecimalField(decimal_places=2, null=False, max_digits=14)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
