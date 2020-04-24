from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank= True)
    photo = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
