from django.db import models
from django.conf import settings

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True, upload_to='files')

    def __str__(self):
        return "File:" + self.name

class Folder(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)

    def __str__(self):
        return "Folder:" + self.path + self.name
