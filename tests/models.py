from django.db import models


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    url = models.URLField("URL")
    notes = models.TextField()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
