from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = None # to force django to login using email insted of username
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []