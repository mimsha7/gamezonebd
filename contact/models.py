from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=155)
    message = models.TextField()
    photo = models.ImageField(upload_to='contact/', blank=True)

    def __str__(self):
        return self.name
