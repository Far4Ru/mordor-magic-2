from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_login', 'id', 'nickname', 'role']


class CharacterSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class CharacterOwnerOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterOwner
        fields = ['owner']


class CharacterCreateSerializer(serializers.ModelSerializer):
    user_characters = CharacterOwnerOwnerSerializer()

    class Meta:
        model = Character
        fields = '__all__'

    def create(self, validated_data):
        character_owner_data = validated_data.pop('user_characters')
        character_instance = Character.objects.create(**validated_data)
        CharacterOwner.objects.create(character=character_instance, **character_owner_data)
        return character_instance


class CharacterOwnerCharacterSerializer(serializers.ModelSerializer):
    character = CharacterSerializer(read_only=True)

    class Meta:
        model = CharacterOwner
        fields = ['character']


class UserCharactersSerializer(serializers.ModelSerializer):
    character_user = CharacterOwnerCharacterSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['nickname', 'character_user']


class CharacterEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterEvent
        fields = '__all__'


class CharacterEventsSerializer(serializers.ModelSerializer):
    character_events = CharacterEventSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = ['nickname', 'character_events']
