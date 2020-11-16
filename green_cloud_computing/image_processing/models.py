from django.db import models

# Create your models here.


class imagesDB(models.Model):
    image_name = models.CharField(blank=False, max_length=20)
    image_url = models.URLField(max_length=200)
    image_time = models.DateTimeField(auto_now=True)
