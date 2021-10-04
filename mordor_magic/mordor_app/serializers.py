from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'nickname', 'role']


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_login', 'id', 'nickname', 'role']


class UserCreateSerializer(serializers.Serializer):
    nickname = serializers.CharField()

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return User(**validated_data)

# TODO: - профиль
# Никнейм
# Имя
# Количество персонажей
# Количество выполненных событий
# Роль
# Почта

# TODO: - персонажи
# персонаж
#   список ивентов

# TODO: - события
# имя
# описание
# период
