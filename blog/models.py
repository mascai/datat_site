from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    videoLink = models.CharField(max_length=200, default='DEFAULT STRING')
    text = models.TextField()

    def __str__(self):
        return self.title
