""" Users Model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

# Utils
from datetime import datetime, timezone, timedelta

class User(AbstractUser):
    """ Extends from Django Abstract User, customed 
    for this example. 
    """

    last_logout = models.DateTimeField(blank=True, null=True)    
    last_session_duration = models.PositiveIntegerField(blank=True, null=True)
    button1_count = models.PositiveIntegerField(default=0)
    button2_count = models.PositiveIntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def update_last_session(self):
        timediff = self.last_logout - self.last_login
        minutes = timediff.seconds//60
        self.last_session_duration = minutes        
        self.save()
        
    def set_as_admin(self):
        self.is_admin = True
        self.save()

    def add_button1(self):
        self.button1_count += 1
        self.save() 

    def add_button2(self):
        self.button2_count += 1
        self.save()

@receiver(user_logged_out)
def set_user_logout(sender, request, user, **kwargs):
    request.user.last_logout = datetime.now(timezone.utc)
    request.user.update_last_session()
    request.user.save()




    



    








