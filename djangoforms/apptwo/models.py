from django.db import models

# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=264)
    body = models.CharField(max_length=264)

    def __str__(self):
        return 'This model '+ self.name