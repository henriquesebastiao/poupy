from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Account
from ..serializers.accounts import AccountSerializer


@api_view()
def get_account(request, id):
    """Obtém uma conta específica pelo ID."""
    accounts = get_object_or_404(Account.objects.filter(id=id))
    serializer = AccountSerializer(instance=accounts, many=False)
    return Response(serializer.data)


@api_view()
def get_all_accounts(request):
    """Obtém todas as contas."""
    accounts = Account.objects.get_queryset()
    serializer = AccountSerializer(instance=accounts, many=True)
    return Response(serializer.data)
