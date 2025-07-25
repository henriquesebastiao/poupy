"""
Os serializers são utilizados para converter instâncias
de modelos Django em formatos JSON ou outros formatos de dados
que podem ser facilmente renderizados em uma resposta HTTP.
Eles são essenciais para a construção de APIs RESTful com Django REST Framework.
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=55)
    balance = serializers.DecimalField(decimal_places=2, max_digits=14)
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    username = serializers.StringRelatedField(source='user.username', read_only=True)
