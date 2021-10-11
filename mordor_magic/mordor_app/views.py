from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Character
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


# @permission_classes([IsAuthenticated])
class CharacterCreateAPIView(generics.CreateAPIView):
    serializer_class = CharacterCreateSerializer
    queryset = Character.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(...)
    #     data = serializer.data
    #     return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class CharacterListAPIView(generics.ListAPIView):
    serializer_class = CharacterOwnerSerializer
    queryset = CharacterOwner.objects.all()

    # def get_queryset(self):
    #     nickname = self.request.GET.get('nickname')
    #     if nickname:
    #         try:
    #             queryset = self.queryset.filter(nickname=nickname)
    #         except ValueError:
    #             queryset = self.Character.objects.none()
    #         return queryset
    #     return self.Character.objects.none()
    # def list(self, request):
    #     queryset = CharacterOwner.objects.filter(owner=request.user)


# @permission_classes([IsAuthenticated])
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class EventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


# @permission_classes([IsAuthenticated])
class UserAPIView(generics.ListAPIView):
    model = User
    serializer_class = UserUpdateSerializer
    queryset = model.objects.all()

    def get_queryset(self):
        username = self.request.GET.get('username')
        # user = self.request.username
        if username:
            try:
                queryset = self.queryset.filter(username=username)
                # User.objects.filter(username=username)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.model.objects.none()

    def patch(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters")


# @permission_classes([IsAuthenticated])
class UserUpdateAPIView(APIView):
    @staticmethod
    def get_object(pk):
        return User.objects.get(pk=pk)

    def patch(self, request, pk):
        user = self.get_object(pk)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters")

# [IsAdminUser]


class UserCharactersAPIView(generics.ListAPIView):
    serializer_class = UserCharactersSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            try:
                queryset = self.queryset.filter(username=username)
                # User.objects.filter(username=username)
            except ValueError:
                queryset = self.User.objects.none()
            return queryset
        return self.User.objects.none()


class CharacterEventsAPIView(generics.ListAPIView):
    serializer_class = CharacterEventsSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        nickname = self.request.GET.get('nickname')
        if nickname:
            try:
                queryset = self.queryset.filter(nickname=nickname)
                # User.objects.filter(username=username)
            except ValueError:
                queryset = self.Character.objects.none()
            return queryset
        return self.Character.objects.none()


class CharacterEventsCountAPIView(generics.ListAPIView):
    serializer_class = CharacterEventsCountSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        nickname = self.request.GET.get('nickname')
        if nickname:
            try:
                queryset = self.queryset.filter(nickname=nickname)
                # User.objects.filter(username=username)
            except ValueError:
                queryset = self.Character.objects.none()
            return queryset
        return self.Character.objects.none()
