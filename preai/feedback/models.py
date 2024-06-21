from django.db import models

class Feedback(models.Model):
    filename = models.CharField(max_length=255)
    result = models.TextField()
    processed_at = models.DateTimeField(auto_now_add=True)
