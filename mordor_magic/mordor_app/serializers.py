from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
    model = Warrior
    fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
       profession = Profession(**validated_data)
       profession.save()
       return Profession(**validated_data)

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["title", "description"]

class SkillRelatedSerializer(serializers.ModelSerializer):
    warrior_skils = WarriorSerializer(many=True)

    class Meta:
        model = Skill
        fields = ["title", "warrior_skils"]