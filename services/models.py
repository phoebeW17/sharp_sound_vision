from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Service(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    description = models.TextField()
    example = models.URLField()
    status = models.IntegerField(choices=STATUS, default=0)
