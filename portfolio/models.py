from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Service(models.Model):
    title = models.CharField(max_length=100)
    media = CloudinaryField('media', default='placeholder')
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)





