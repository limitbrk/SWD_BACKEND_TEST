from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    done = models.BooleanField(null=False, blank=False, default=False)
