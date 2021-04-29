from django.db import models
from django.contrib.auth.models import AbstractUser,Group


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    phone = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
