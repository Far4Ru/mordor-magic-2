from django.shortcuts import render
from rest_framework.views import APIView
from .models import Warrior, Profession
from .serializers import WarriorSerializer, ProfessionCreateSerializer
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.
class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)
        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()
        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()
