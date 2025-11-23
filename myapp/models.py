from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Image(models.Model):
    # photo = models.ImageField(upload_to='myimage')
    photo = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add= True)
    
    