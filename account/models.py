from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='defult.png',upload_to='profile')


