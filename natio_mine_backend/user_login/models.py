from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser): 
    profile = models.ForeignKey(
    'profile_api.Profile',
    on_delete=models.CASCADE,
    null=True
    )