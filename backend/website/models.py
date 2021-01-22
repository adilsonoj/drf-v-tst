from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    created_at = models.DateField()
