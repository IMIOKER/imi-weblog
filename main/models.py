from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default = None)
    cat = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[0:100] + ' ...'
