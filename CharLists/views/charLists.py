from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework.viewsets import ViewSet
from rest_framework import authentication, permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from CharLists.models import charList , gameClass, gameRace
from CharLists.serializers import charListSerializer


class CharLists(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        UserId = Token.objects.get(key=request.auth.key).user.pk

        charLists  = charList.objects.filter(user=UserId)
        serialized = charListSerializer(charLists, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json);

    def isCompleteRequest(self, request):
        return False

    def add(self, request):
        UserId = Token.objects.get(key=request.auth.key).user.pk
        if (self.isCompleteRequest(request)):
            return Response({'ok': 'False'});
        else:
            cl = charList(
                user= User.objects.get(id = UserId),

                name = request.data['name'],
                description=request.data['description'],

                strength     = request.data['strength'],
                dexterity    = request.data['dexterity'],
                constitution = request.data['constitution'],
                intelegency  = request.data['intelegency'],
                wisdom       = request.data['wisdom'],
                charisma     = request.data['charisma'],

                gameClassMain = gameClass.objects.get(id = request.data['gameClassMain']),
                gameRace      = gameRace.objects.get (id = request.data['gameRace'])
            );
            if 'background' in request.data:
                cl.background = request.data['background']
            if 'alignment' in request.data:
                cl.alignment = request.data['alignment']
            if 'img' in request.data:
                cl.img = request.data['img']

            cl.save();
            return Response({'ok': 'True'});
