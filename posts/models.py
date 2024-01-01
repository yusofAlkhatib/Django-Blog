from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    creatrd_at = models.DateTimeField(default=timezone.now)