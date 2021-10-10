from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    roles = (
        ('1', 'Глава'),
        ('2', 'Зам. главы'),
        ('3', 'Офицер'),
        ('4', 'Элита'),
        ('5', 'Участник'),
    )
    nickname = models.CharField(max_length=30, null=True, unique=True)
    role = models.CharField(choices=roles, max_length=1, null=True, default='5')
    registration_status = models.BooleanField(null=True)
    user_online_date = models.DateField(null=True)


class Character(models.Model):
    types = (
        ('1', 'Основа'),
        ('2', 'Твин'),
        ('3', 'Репутация')
    )
    nickname = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=45)
    type = models.CharField(choices=types, max_length=1, null=True, default='2')


class CharacterOwner(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='character_user', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='user_characters', on_delete=models.CASCADE)


class Event(models.Model):
    periods = (
        ('d', 'day'),
        ('w', 'week'),
        ('m', 'month')
    )
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    period = models.CharField(choices=periods, max_length=1)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    max_value = models.IntegerField(null=True)
    color = models.CharField(max_length=30, null=True)


class CharacterEvent(models.Model):
    character = models.ForeignKey(Character, related_name='character_events', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    status = models.BooleanField()
    date = models.DateField()
    value = models.IntegerField(null=True)
