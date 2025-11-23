from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
    title = models.CharField(max_length=100, blank=True)
    photo = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"

    
