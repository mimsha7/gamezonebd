from django.db import models
from datetime import datetime

class Forum(models.Model):
    name = models.CharField(max_length=150)
    post = models.TextField()
    avatar = models.ImageField(upload_to='forum_avatar',default='forum_avatar/defult.png', blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

