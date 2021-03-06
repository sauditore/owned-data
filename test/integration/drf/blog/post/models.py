from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return f"User: {self.author.id}, Post: {self.title}"
