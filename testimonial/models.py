from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# project choices for user in testimonial project type drop down list in tuple format
# value and site viewable value for users
PROJECT_CHOICES = [ 
    ('brand_videos', 'Brand Videos'), 
    ('explainer_videos', 'Explainer Videos'), 
    ('photography', 'Photography'),
    ('social_media_content', 'Social Media Content'), 
] 

STATUS = ((0, "Draft"), (1, "Published"))

class Testimonial(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    project_type = models.CharField(max_length=30, choices=PROJECT_CHOICES, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return f"{self.title} | written by {self.user}"