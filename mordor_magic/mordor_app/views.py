from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.response import Response
from rest_framework import generics


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
