from django.conf.urls import url
from django.urls import path, include
from .views import *

urlpatterns = [
   path('users/', MembersListAPIView.as_view()),
   path('users/user', UserAPIView.as_view()),
   path('users/create/', UserCreateAPIView.as_view()),
   url(r'^auth/', include('djoser.urls')),
   url(r'^auth/', include('djoser.urls.authtoken')),
]
