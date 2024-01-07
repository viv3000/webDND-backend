from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.viewsets import ViewSet
from rest_framework import authentication, permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from CharLists.models import gameClass, gameRace, background
from CharLists.serializers import gameClassSerializer, gameRaceSerializer, backgroundSerializer


def classList(request):
        gameClasses = gameClass.objects.all();
        serialized = gameClassSerializer(gameClasses, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

def raceList(request):
        gameRaces = gameRace.objects.all();
        serialized = gameRaceSerializer(gameRaces, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

def backgroundList(request):
        backgrounds = background.objects.all();
        serialized = backgroundSerializer(backgrounds, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

