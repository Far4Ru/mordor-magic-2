from django.db import models

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
    nickname = models.CharField(max_length=30)
    role = models.CharField(choices=roles, max_length=1)


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipient = models.IntegerField()
    text = models.CharField(max_length=255)
    date = models.DateField()


class Task(models.Model):
    periods = (
        ('d', 'day'),
        ('w', 'week'),
        ('m', 'month'),
        ('y', 'year'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)
    time = models.CharField(max_length=5)
    period = models.CharField(choices=periods, max_length=1)


class Checklist(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField
    status = models.CharField(max_length=1)
