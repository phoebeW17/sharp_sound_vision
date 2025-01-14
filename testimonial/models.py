from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Testimonial(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    project = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)