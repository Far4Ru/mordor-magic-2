from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('user/update/', UserUpdateAPIView.as_view()),
    # path('user/delete/', 0),
    path('user/characters/', UserCharactersAPIView.as_view()),
    path('characters/', CharacterListAPIView.as_view()),
    path('characters/create/', CharacterCreateAPIView.as_view()),
    path('character/events/', CharacterEventsAPIView.as_view()),
    path('character/events/count/', CharacterEventsCountAPIView.as_view()),
    # path('character/users/', 0),
    # path('character/update/', 0),
    # path('character/delete/', 0),
    path('events/', EventListAPIView.as_view()),
    # path('event/characters/', 0),
    # path('event/create/', 0),
    # path('event/update/', 0),
    # path('event/delete/', 0),
    # path('character_owners/', 0),
    # path('character_events/', 0),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
