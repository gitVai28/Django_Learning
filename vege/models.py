from django.db import models
# The User model is Django's default user authentication model, which is part of the django.contrib.auth module.
# It provides built-in authentication features like user registration, login, logout, and password management.
'''


'''
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    #model.CASCADE means if any user deletes its account then all the receipes uploaded by him/her will be deleted
    #model.SET_NULL means it set null value at the place of user receipes
    #model.SET_DEFAULT means it sets default values
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="receipe")