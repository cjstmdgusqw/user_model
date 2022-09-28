from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomModel(AbstractUser):
    class Meta:
        db_table = "custom_user"
    address = models.CharField('주소', max_length=500, blank=True)
    bio = models.CharField('내용', max_length=500, blank=True)
