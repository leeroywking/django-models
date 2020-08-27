from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=64) #charfield max len 64 characters
    author = models.ForeignKey("auth.user", default=1, on_delete=models.CASCADE) # feirgnkey user model with cascade
    body = models.TextField()#text field

    def __str__(self):
        return self.title