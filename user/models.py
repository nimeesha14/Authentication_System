from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return {self.first_name, self.last_name}


class UserProfile(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    project_url = models.URLField()
    project_description = models.TextField()


    def __str__(self):
        return {self.project_name}



# Create your models here.
