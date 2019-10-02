from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    url = models.URLField("URL")
    notes = models.TextField()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
