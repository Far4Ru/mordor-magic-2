from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, MembersSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import authenticate, login,logout
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MembersListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MembersSerializer
    queryset = User.objects.all()


class UserAPIView(generics.ListAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = model.objects.all()

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            try:
                queryset = self.queryset.filter(username=username)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.model.objects.none()
