""" Users URLs. """

# Django
from django.urls import path
from django.conf.urls import include, url

# Django REST Framework
from rest_framework import routers

# Views
from . import views


router = routers.SimpleRouter()
router.register('users', views.UserViewSet, basename='users')


urlpatterns = router.urls

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]