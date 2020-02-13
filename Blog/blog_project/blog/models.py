from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
    	return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default="default.jpg")
    content = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    modified_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
    	return self.title

