from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/', UserUpdateAPIView.as_view()),
    path('user/characters/', UserCharactersAPIView.as_view()),
    # path('users/create/', UserCreateAPIView.as_view()),
    path('characters/', CharacterListAPIView.as_view()),
    path('characters/create/', CharacterCreateAPIView.as_view()),
    path('character/events/', CharacterEventsAPIView.as_view()),
    path('character/events/count/', CharacterEventsCountAPIView.as_view()),
    # path('characters/update/'),
    # path('characters/delete/'),
    path('events/', EventListAPIView.as_view()),
    # path('events/create/'),
    # path('events/update/'),
    # path('events/delete/'),
    # path('character/events/'),
    # path('character/events/create/'),
    # path('character/events/update/'),
    # path('character/events/delete/'),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
