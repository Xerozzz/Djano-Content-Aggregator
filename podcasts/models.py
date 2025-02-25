from django.db import models

# Create your models here.
class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    image = models.URLField()
    link = models.URLField()
    podcast_name = models.CharField(max_length=200)
    guid = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.podcast_name}: {self.title}"