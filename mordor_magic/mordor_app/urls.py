from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('user/characters/', UserCharactersAPIView.as_view()),
    path('user/characters/events/', UserCharacterEventsAPIView.as_view()),
    path('characters/', CharacterListAPIView.as_view()),
    path('characters/create/', CharacterCreateAPIView.as_view()),
    path('character/events/', CharacterEventsAPIView.as_view()),
    path('character/events/count/', CharacterEventsCountAPIView.as_view()),
    path('events/', EventListAPIView.as_view()),
    path('character_owners/', CharacterOwnersListAPIView.as_view()),
    path('character_events/', CharacterEventsListAPIView.as_view()),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
