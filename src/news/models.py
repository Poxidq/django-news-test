from django.db import models


class Favorite(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(default="")
    url = models.URLField()
    published_at = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.title
