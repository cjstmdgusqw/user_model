from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomModel(AbstractUser):
    class Meta:
        db_table = "custom_user"
    address = models.TextField('주소', max_length=5000, blank=True)
    bio = models.TextField('내용', max_length=500, blank=True)
