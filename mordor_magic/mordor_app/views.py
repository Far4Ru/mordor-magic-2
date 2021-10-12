from datetime import datetime
from itertools import chain

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Character
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


@permission_classes([IsAuthenticated])
class CharacterCreateAPIView(generics.CreateAPIView):
    serializer_class = CharacterCreateSerializer
    queryset = Character.objects.all()


@permission_classes([IsAuthenticated])
class CharacterListAPIView(generics.ListAPIView):
    serializer_class = CharacterPublicSerializer
    model = Character
    queryset = Character.objects.all()


@permission_classes([IsAuthenticated])
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@permission_classes([IsAuthenticated])
class EventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    model = Event

    def get_queryset(self):
        date = self.request.GET.get('date')
        if date:
            try:
                date_time_obj = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
                queryset = self.queryset.filter(period="d")
                queryset_week2 = self.queryset.filter(period="w")\
                    .filter(period_across=2)\
                    .filter(period_parity=date_time_obj.timetuple().tm_yday // 7 % 2)\
                    .filter(start_date__iso_week_day=date_time_obj.weekday())
                queryset_week1 = self.queryset.filter(period="w")\
                    .filter(period_across=1)\
                    .filter(start_date__iso_week_day=date_time_obj.isoweekday())
                queryset = list(chain(queryset, queryset_week1, queryset_week2))
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.model.objects.all()


@permission_classes([IsAuthenticated])
class UserAPIView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()

    def get_queryset(self):
        username = self.request.GET.get('username')
        if not username:
            username = self.request.user.username
        if username:
            try:
                queryset = self.queryset.filter(username=username)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.model.objects.none()

    @staticmethod
    def patch(request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters")


@permission_classes([IsAuthenticated])
class UserCharactersAPIView(generics.ListAPIView):
    serializer_class = UserCharactersSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            try:
                queryset = self.queryset.filter(username=username)
            except ValueError:
                queryset = self.User.objects.none()
            return queryset
        return self.User.objects.none()


@permission_classes([IsAuthenticated])
class CharacterEventsAPIView(generics.ListAPIView):
    serializer_class = CharacterEventsSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        nickname = self.request.GET.get('nickname')
        if nickname:
            try:
                queryset = self.queryset.filter(nickname=nickname)
            except ValueError:
                queryset = self.Character.objects.none()
            return queryset
        return self.Character.objects.none()


@permission_classes([IsAuthenticated])
class UserCharacterEventsAPIView(generics.ListAPIView):
    serializer_class = CharacterOwnerSerializer
    queryset = CharacterOwner.objects.all()

    def list(self, request):
        date = self.request.GET.get('date')
        inner_character_event = CharacterEvent.objects.filter(date=date)
        inner_character = Character.objects.filter(character_events__in=inner_character_event)
        queryset = CharacterOwner.objects.filter(owner=request.user).filter(character__in=inner_character)
        serializer = UserCharacterEventsSerializer(queryset, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class CharacterEventsCountAPIView(generics.ListAPIView):
    serializer_class = CharacterEventsCountSerializer
    queryset = Character.objects.all()

    def get_queryset(self):
        nickname = self.request.GET.get('nickname')
        if nickname:
            try:
                queryset = self.queryset.filter(nickname=nickname)
            except ValueError:
                queryset = self.Character.objects.none()
            return queryset
        return self.Character.objects.none()


@permission_classes([IsAuthenticated])
class CharacterOwnersListAPIView(generics.ListAPIView):
    serializer_class = CharacterOwnerSerializer
    queryset = CharacterOwner.objects.all()


@permission_classes([IsAuthenticated])
class CharacterEventsListAPIView(generics.ListAPIView):
    serializer_class = CharacterEventSerializer
    queryset = CharacterEvent.objects.all()
