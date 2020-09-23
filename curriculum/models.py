from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    author = models.CharField(default="", max_length=25)
    quote = models.TextField(default="", max_length=100)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
