from django.urls import include, path
from rest_framework.authtoken import views

from CharLists.views.charLists import *
from CharLists.views.DNDInformation import classList, raceList, backgroundList

urlpatterns = [
    path('api/CharLists/', CharLists.as_view({'get': 'list'}), name='Persons'),
    path('api/CharLists/Add', CharLists.as_view({'post': 'add'}), name='PersonAdd'),
    path('api/CharLists/Classes', classList),
    path('api/CharLists/Races', raceList),
    path('api/CharLists/Backgrounds', backgroundList),
    path('api-token-auth/', views.obtain_auth_token), # curl --data "username=username&password=password" http://127.0.0.1:8000/api/api-token-auth/
]