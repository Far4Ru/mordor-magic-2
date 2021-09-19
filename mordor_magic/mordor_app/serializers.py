from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.Serializer):
    nickname = serializers.CharField()

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return User(**validated_data)
