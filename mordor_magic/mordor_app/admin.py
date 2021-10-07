from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(CharacterEvent)
admin.site.register(Event)
admin.site.register(CharacterOwner)
admin.site.register(Character)
admin.site.register(User, UserAdmin)
