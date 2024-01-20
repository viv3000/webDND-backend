from django.urls import include, path
from rest_framework.authtoken import views

from CharLists.views.charLists import *
from CharLists.views.DNDInformation import alignmentList, classList, raceList, backgroundList, gameClassForId, gameRaceForId, alignmentForId, backgroundForId

urlpatterns = [
    path('api/CharLists/',     CharLists.as_view({'get': 'list'}), name='Persons'),
    path('api/CharLists',      CharLists.as_view({'get': 'list'}), name='Persons'),
    path('api/CharLists/<int:id>',  CharLists.as_view({'get': 'person'}), name='Persons'),
    path('api/CharLists/<int:id>/', CharLists.as_view({'get': 'person'}), name='Persons'),
    path('api/CharLists/Add',  CharLists.as_view({'post': 'add'}), name='PersonAdd'),
    path('api/CharLists/Add/', CharLists.as_view({'post': 'add'}), name='PersonAdd'),
    path('api/CharLists/Update/<int:id>',  CharLists.as_view({'post': 'update'}), name='PersonAdd'),
    path('api/CharLists/Update/<int:id>/', CharLists.as_view({'post': 'update'}), name='PersonAdd'),
    path('api/CharLists/Delete/<int:id>',  CharLists.as_view({'post': 'delete'}), name='PersonAdd'),
    path('api/CharLists/Delete/<int:id>/', CharLists.as_view({'post': 'delete'}), name='PersonAdd'),
    path('api/CharLists/Race/<int:id>',  gameRaceForId),
    path('api/CharLists/Race/<int:id>/', gameRaceForId),
    path('api/CharLists/Class/<int:id>',  gameClassForId),
    path('api/CharLists/Class/<int:id>/', gameClassForId),
    path('api/CharLists/Alignment/<int:id>',  alignmentForId),
    path('api/CharLists/Alignment/<int:id>/', alignmentForId),
    path('api/CharLists/Background/<int:id>',  backgroundForId),
    path('api/CharLists/Background/<int:id>/', backgroundForId),
    path('api/CharLists/Classes',  classList),
    path('api/CharLists/Classes/', classList),
    path('api/CharLists/Races',  raceList),
    path('api/CharLists/Races/', raceList),
    path('api/CharLists/Alignments',  alignmentList),
    path('api/CharLists/Alignments/', alignmentList),
    path('api/CharLists/Backgrounds',  backgroundList),
    path('api/CharLists/Backgrounds/', backgroundList),
    path('api-token-auth/', views.obtain_auth_token), # curl --data "username=username&password=password" http://127.0.0.1:8000/api/api-token-auth/
]
