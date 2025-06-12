from django.contrib import admin
from .models import *


@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'city', 'phone')
    search_fields = ('user__username', 'city', 'hobby')
    list_filter = ('city',)




