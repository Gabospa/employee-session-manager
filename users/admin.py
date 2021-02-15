""" Users admin"""
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import User

class CustomUserAdmin(UserAdmin):
    """ User model admin"""

    list_display = ('username', 'first_name', 'last_name', 'last_session_duration', 'is_admin')

admin.site.register(User, CustomUserAdmin)
