from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    contact = models.IntegerField(default=0 ,null=False)
    location = models.CharField(max_length=20,null=False,default='')

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)


    def __str__(self):
        return self.user.username

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return self.user.username