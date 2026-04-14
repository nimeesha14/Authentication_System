from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager



class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=50,unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)


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




class Document(models.Model):
    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('doc', 'DOC'),
        ('img', 'Image'),
    ]

    file = models.FileField(upload_to='')
    name = models.CharField(max_length=255)

    file_type = models.CharField(
        max_length=10,
        choices=FILE_TYPE_CHOICES,
        default='pdf'
    )

    size = models.PositiveIntegerField(help_text="Size in KB")

    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='documents_added'
    )
    added_date = models.DateTimeField(auto_now_add=True)

    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='documents_updated'
    )
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
