from django.conf.urls import url
from django.urls import path, include
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('users/', UserListAPIView.as_view()),
   path('users/create/', UserCreateAPIView.as_view()),
   url(r'^auth/', include('djoser.urls')),
   url(r'^auth/', include('djoser.urls.authtoken')),
]
