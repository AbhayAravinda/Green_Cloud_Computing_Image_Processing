from djongo import models

# Create your models here.


class imagesDB(models.Model):
    image = models.ImageField(upload_to="")
    image_time = models.DateTimeField(auto_now=True)
