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


class CharacterSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class CharacterCreateSerializer(serializers.ModelSerializer):

    class CharacterOwnerCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = CharacterOwner
            fields = ['owner']

    character_owner = CharacterOwnerCreateSerializer()

    class Meta:
        model = Character
        fields = '__all__'

    def create(self, validated_data):
        character_owner_data = validated_data.pop('character_owner')
        print(character_owner_data)
        character_instance = Character.objects.create(**validated_data)
        print(character_instance)
        CharacterOwner.objects.create(character=character_instance, **character_owner_data)
        return character_instance