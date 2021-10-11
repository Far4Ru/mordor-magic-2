from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        model = User
        fields = ['last_login', 'nickname', 'role', 'first_name', 'registration_status', 'user_online_date', 'last_name', 'email']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['id']


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['nickname', 'first_name', 'last_name']


class CharacterSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Character
        exclude = ['id']


class CharacterPublicSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Character
        exclude = ['id', 'email']


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
    character = CharacterPublicSerializer(read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = CharacterOwner
        exclude = ['id']


class UserCharactersSerializer(serializers.ModelSerializer):
    character_user = CharacterOwnerCharacterSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['nickname', 'character_user']


class CharacterEventSerializer(serializers.ModelSerializer):
    character = CharacterPublicSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = CharacterEvent
        exclude = ['id']


class CharacterEventOnlySerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = CharacterEvent
        exclude = ['id', 'character']


class CharacterEventsSerializer(serializers.ModelSerializer):
    character_events = CharacterEventOnlySerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = ['nickname', 'character_events']


class UserCharacterEventsSerializer(serializers.ModelSerializer):
    character = CharacterEventsSerializer(read_only=True)

    class Meta:
        model = CharacterOwner
        fields = ['character']


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
