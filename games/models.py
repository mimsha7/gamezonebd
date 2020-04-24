from django.db import models
from datetime import datetime

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='games/', blank=True)
    review_int = models.DecimalField(max_digits=2, decimal_places=1)
    review_str = models.PositiveIntegerField(default=0)
    release_date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=122, null=True)
    about = models.TextField(blank=True)
    platform = models.CharField(max_length=250, null=True)
    developer = models.CharField(max_length=120, null=True)
    publisher = models.CharField(max_length=110, null=True)
    sys_requirement = models.TextField(null=True)

    def __str__(self):
        return self.name
