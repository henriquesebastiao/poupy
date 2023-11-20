from django.contrib import admin

from .models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'balance',
        'user_id',
        'created_at',
        'updated_at',
    ]
    list_display_links = ['name']
    search_fields = ['name', 'balance', 'created_at', 'updated_at', 'user_id']
    list_filter = ['name', 'created_at', 'updated_at', 'user_id']
    list_per_page = 10
    ordering = ['-id']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'description',
        'value',
        'user_id',
        'account_id',
        'transaction_date',
        'created_at',
        'updated_at',
    ]
    list_display_links = ['description']
    search_fields = [
        'type',
        'description',
        'value',
        'user_id',
        'account_id',
        'transaction_date',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'type',
        'user_id',
        'account_id',
        'transaction_date',
        'created_at',
        'updated_at',
    ]
    list_per_page = 10
    ordering = ['-id']
