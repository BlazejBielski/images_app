from django.db import models

from config import settings
from images.validators import validate_file_type


class Image(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.FileField(upload_to='images/', validators=[validate_file_type])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.url.name
        return super().save(*args, **kwargs)


class Thumbnail(models.Model):
    image = models.ForeignKey('Image', related_name='thumbnails', on_delete=models.CASCADE)
    url = models.FileField(upload_to='resized_images/')
    height = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.url.name}'
