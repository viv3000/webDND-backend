from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.viewsets import ViewSet
from rest_framework import authentication, permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from CharLists.models import gameClass, gameRace, background, alignment
from CharLists.serializers import gameClassSerializer, gameRaceSerializer, backgroundSerializer, alignmentSerializer


def alignmentForId(request, id):
        alignments = alignment.objects.filter(id=id);
        serialized = alignmentSerializer(alignments, many=True)
        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

def gameRaceForId(request, id):
        gameRaces = gameRace.objects.filter(id=id);
        serialized = gameRaceSerializer(gameRaces, many=True)
        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

def gameClassForId(request, id):
        gameClasses = gameClass.objects.filter(id=id);
        serialized = gameClassSerializer(gameClasses, many=True)
        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

def backgroundForId(request, id):
        backgrounds = background.objects.filter(id=id);
        serialized = backgroundSerializer(backgrounds, many=True)
        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

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

def alignmentList(request):
        alignments = alignment.objects.all();
        serialized = alignmentSerializer(alignments, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

def backgroundList(request):
        backgrounds = background.objects.all();
        serialized = backgroundSerializer(backgrounds, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json)

