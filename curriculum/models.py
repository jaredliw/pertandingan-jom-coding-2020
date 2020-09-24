from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    author = models.CharField(default="Anonim", max_length=25, blank=False)
    quote = models.TextField(max_length=100, blank=False)

class Comment(models.Model):
    username = models.CharField(default="Anonim", max_length=30, blank=False)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
