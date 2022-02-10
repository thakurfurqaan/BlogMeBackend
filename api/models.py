
from django.db import models

# Create your models here.

# class Article(models.Model):
#     # _id = models.IntegerField(primary_key=True, auto_created=True)
#     userId = models.IntegerField(default=0)
#     _id = models.IntegerField(default=0)
#     title = models.CharField(max_length=100)
#     description = models.TextField(default="")
#     body = models.TextField(default="")

#     def __str__(self):
#         return self.title

class Post(models.Model):
    _id = models.AutoField(primary_key=True)
    userId = models.IntegerField(default=0)
    id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    body = models.TextField(default="")

    def __str__(self):
        return self.title
