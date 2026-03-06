from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager



class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=50,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return f"{self.email}"


class UserProfile(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    project_url = models.URLField()
    project_description = models.TextField()


    def __str__(self):
        return self.project_name



# Create your models here.
