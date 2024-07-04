from django.db import models


# Create your models here.
class Favorite(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.title
