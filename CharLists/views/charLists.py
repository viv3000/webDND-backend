from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework.viewsets import ViewSet
from rest_framework import authentication, permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

import io

from CharLists.models import charList , gameClass, gameRace, background, alignment
from CharLists.serializers import charListImgSerializer

class CharLists(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def person(self, request, id):
        UserId = Token.objects.get(key=request.auth.key).user.pk

        charLists  = charList.objects.filter(user=UserId, id=id)
        serialized = charListImgSerializer(charLists, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json);


    def list(self, request):
        UserId = Token.objects.get(key=request.auth.key).user.pk

        charLists  = charList.objects.filter(user=UserId)
        serialized = charListImgSerializer(charLists, many=True)

        json = renderers.JSONRenderer().render(serialized.data)
        return HttpResponse(json);

    def update(self, request, id):
        UserId = Token.objects.get(key=request.auth.key).user.pk
        if (not self.isCompleteRequest(request)):
            return Response({'ok': 'False'}, status=400);
        else:
            cl = charList.objects.get(id = id);
            cl.user= User.objects.get(id = UserId)

            cl.name = request.data['name']
            cl.description=request.data['description']

            cl.strength     = request.data['strength']
            cl.dexterity    = request.data['dexterity']
            cl.constitution = request.data['constitution']
            cl.intelegency  = request.data['intelegency']
            cl.wisdom       = request.data['wisdom']
            cl.charisma     = request.data['charisma']

            cl.gameClassMain = gameClass.objects.get(id = request.data['gameClassMain'])
            cl.gameRace      = gameRace.objects.get (id = request.data['gameRace'])

            if 'background' in request.data:
                cl.background = background.objects.get(id = request.data['background'])
            if 'alignment' in request.data:
                cl.alignment = alignment.objects.get(id = request.data['alignment'])
            if 'img' in request.data:
                cl.img = request.FILES['img']
            cl.save();
            return Response({'ok': 'True'});

    def delete(self, request, id):
        try:
            UserId = Token.objects.get(key=request.auth.key).user.pk
            print(charList.objects.filter(user=UserId, id=id))
            charList.objects.filter(user=UserId, id=id).delete()
            return Response({'ok': 'True'});
        except:
            return Response({'ok': 'False'}, status=300);

    def add(self, request):
        UserId = Token.objects.get(key=request.auth.key).user.pk
        if (not self.isCompleteRequest(request)):
            return Response({'ok': 'False'}, status=400);
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
                cl.background = background.objects.get(id = request.data['background'])
            if 'alignment' in request.data:
                cl.alignment = alignment.objects.get(id = request.data['alignment'])
            if 'img' in request.data:
                print(type(request.data['img'].field_name))
                print(request.data['img'].charset)
                print(request.data['img'].file)
                print(type(cl.img))
                print(type(request.FILES['img']))
                cl.img = request.FILES['img']
            cl.save();
            return Response({'ok': 'True'});

    def isCompleteRequest(self, request):
        return True

