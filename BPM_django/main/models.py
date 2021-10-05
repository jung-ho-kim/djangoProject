from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    userBirth = models.IntegerField(default=0)
    userWeight = models.IntegerField(default=0)
    userHeight = models.IntegerField(default=0)

'''
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    userBirth = models.IntegerField(default=0)
    userWeight = models.IntegerField(default=0)
    userHeight = models.IntegerField(default=0)
'''