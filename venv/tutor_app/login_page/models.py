from django.db import models

# Create your models here.
class images(models.Model):
    image = models.FilePathField(path="/img")
