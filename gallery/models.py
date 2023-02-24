from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/", null=True, blank=True)
    image_url = models.URLField(null=True, blank=True, editable=False)
    created_date =  models.DateTimeField(auto_now_add=True)