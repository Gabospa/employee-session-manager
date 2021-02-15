""" Users views."""

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# Models
from .models import User    

# Serializers
from .serializers import UserModelSerializer, UserLoginSerialzier


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset for listing users
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['login']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """ User login """
        serializer = UserLoginSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def add_button1(self, request, *args, **kwargs):
        """ Increment button 1"""
        user = self.get_object()
        user.add_button1()
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def add_button2(self, request, *args, **kwargs):
        """ Increment button 2"""
        user = self.get_object()
        user.add_button2()
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)