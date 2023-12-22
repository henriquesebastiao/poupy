from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Account, Transaction, Transfer


class ModelTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(
            username='test',
            password='test',
        )

        self.account1 = Account.objects.create(
            name='Account Mixin',
            balance=100.00,
            user=self.u,
        )

        self.account2 = Account.objects.create(
            name='Account Mixin 2',
            balance=100.00,
            user=self.u,
        )

    def test_account_creation(self):
        account = Account.objects.create(
            name='Account',
            balance=100.00,
            user=self.u,
        )

        self.assertTrue(isinstance(account, Account))
        self.assertEqual(account.__str__(), account.name)

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            description='Transaction',
            value=10.00,
            account=self.account1,
            user=self.u,
        )

        self.assertTrue(isinstance(transaction, Transaction))
        self.assertEqual(transaction.__str__(), transaction.description)

    def test_transfer_creation(self):
        transfer = Transfer.objects.create(
            description='Transfer',
            value=10.00,
            account_origin=self.account1,
            account_destination=self.account2,
            user=self.u,
        )

        self.assertTrue(isinstance(transfer, Transfer))
        self.assertEqual(transfer.__str__(), transfer.description)
