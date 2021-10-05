from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, MembersSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


@permission_classes([IsAuthenticated])
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


@permission_classes([IsAuthenticated])
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@permission_classes([IsAuthenticated])
class MembersListAPIView(generics.ListAPIView):
    serializer_class = MembersSerializer
    queryset = User.objects.all()


@permission_classes([IsAuthenticated])
class UserAPIView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
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


@permission_classes([IsAuthenticated])
class UserView(APIView):
    @staticmethod
    def get_object(pk):
        return User.objects.get(pk=pk)

    def patch(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data="wrong parameters")

# [IsAdminUser]
