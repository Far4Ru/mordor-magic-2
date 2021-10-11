from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = User
        fields = ['last_login', 'id', 'nickname', 'role']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'nickname', 'first_name', 'last_name']


class CharacterSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class CharacterOwnerOwnerSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = CharacterOwner
        fields = ['owner']


class CharacterOwnerOwnerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterOwner
        fields = ['owner']


class CharacterCreateSerializer(serializers.ModelSerializer):
    user_characters = CharacterOwnerOwnerCreateSerializer()

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


class CharacterOwnersSerializer(serializers.ModelSerializer):
    user_characters = CharacterOwnerOwnerSerializer()

    class Meta:
        model = Character
        fields = ['nickname', 'email', 'type', 'user_characters']


class CharacterOwnerSerializer(serializers.ModelSerializer):
    character = CharacterSerializer(read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = CharacterOwner
        fields = '__all__'


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


class CharacterEventsCountSerializer(serializers.ModelSerializer):
    # character_events = CharacterEventSerializer(read_only=True, many=True)
    character_events_count = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = ['nickname', 'character_events_count']

    @staticmethod
    def get_character_events_count(obj):
        complete = obj.character_events.all().filter(status=True)
        return complete.count()
