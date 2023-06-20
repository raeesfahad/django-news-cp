from django.db import models
from django.contrib.auth.models import User



class category(models.Model):
     name = models.CharField(max_length=100)
     created = models.DateTimeField(auto_now=True)
     updated = models.DateTimeField(auto_now_add=True)


     def __str__(self):
          return self.name


class News(models.Model):


     title = models.CharField(max_length=50)
     content = models.CharField(max_length=2000)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     created = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)
