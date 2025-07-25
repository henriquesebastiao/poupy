"""
Os serializers são utilizados para converter instâncias
de modelos Django em formatos JSON ou outros formatos de dados
que podem ser facilmente renderizados em uma resposta HTTP.
Eles são essenciais para a construção de APIs RESTful com Django REST Framework.
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'balance', 'user', 'username']

    username = serializers.SerializerMethodField(method_name='get_username', read_only=True)

    def get_username(self, account):
        """Obtém o nome de usuário do usuário associado à conta."""
        user = get_user_model().objects.filter(id=account.user.id).first()
        return user.username if user else None
