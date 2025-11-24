from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.utils import cloudinary_url

class Image(models.Model):
    title = models.CharField(max_length=100, blank=True)
    photo = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add=True)

   @property
    def permanent_url(self):
        url, options = cloudinary_url(self.photo.public_id, secure=True)
        return url

    def __str__(self):
        return self.title or f"Image {self.id}"

    
