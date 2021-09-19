from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('users/', UserListAPIView.as_view()),
   path('users/create/', UserCreateAPIView.as_view()),
]
