from django.db import models

class Post(models.Model):
    file = models.FileField()
