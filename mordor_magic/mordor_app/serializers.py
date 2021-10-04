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
