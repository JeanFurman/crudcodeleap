from django.db import models
from django.utils import timezone

class Career(models.Model):
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()