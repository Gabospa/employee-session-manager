""" Users serializers """

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer."""

    class Meta:
        """ Meta class"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'last_login',
            'last_session_duration',
            'button1_count',
            'button2_count',
            'is_admin'
            )

class UserLoginSerialzier(serializers.Serializer):
    """ User login serializer
    Handles request login data
    """

    username = serializers.CharField(min_length=4, max_length=20)
    password = serializers.CharField(min_length=4, max_length=20)

    def validate(self, data):
        """ Check login data."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')

        self.context['user'] = user
        return data

    def create(self, data):
        """ Generate new token. """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key