from django.db import models

class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    source = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    date_published = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
