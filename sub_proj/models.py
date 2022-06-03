from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Member(models.Model):
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.email + " " + self.username