from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField #https://django-tinymce.readthedocs.io/en/latest/installation.html
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField #https://django-embed-video.readthedocs.io/en/latest/installation.html



# Create your models here.

CM_STATUS = ((1, 'Enable'), (0, 'Disable'))

class doctorCategory(models.Model):
    name = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SocietyMember(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True,null=True, default=None)
    image = models.ImageField(upload_to="society-member/", null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    status = models.SmallIntegerField(choices=CM_STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)

class YoutubeVideo(models.Model):
    youtube_title = models.CharField(max_length=255)
    youtube_link = EmbedVideoField()
    description = HTMLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='youtube_title', unique=True,null=True, default=None)
    created_date =  models.DateTimeField(auto_now_add=True)

class Banner(models.Model):
    banner_img = models.ImageField(upload_to="banner/", null=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    sub_heading = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    link_text = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(choices=CM_STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True,null=True, default=None)
    image = models.ImageField(upload_to="doctors/", null=True, blank=True)
    department = models.ForeignKey(doctorCategory, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    description = HTMLField(null=True, blank=True)
    created_date =  models.DateTimeField(auto_now_add=True)

class Contactus(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    father_name = models.CharField(max_length=50,null=True, blank=True)
    address = models.CharField(max_length=300,null=True, blank=True)
    aadhar_no = models.CharField(max_length=12,null=True, blank=True)
    mobile = models.BigIntegerField()
    whatsapp_no = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True)
    created_date =  models.DateTimeField(auto_now_add=True)
    
class AboutHemophilia(models.Model):
    edit = models.CharField(max_length=50, default="Edit",null=True, blank=True,editable=False)
    image = models.ImageField(upload_to="hemophilia/",null=True, blank=True)
    english = HTMLField(null=True, blank=True,)
    hindi = HTMLField(null=True, blank=True)
    created_date =  models.DateTimeField(auto_now_add=True)
    
class HistoryHemophilia(models.Model):
    edit = models.CharField(max_length=50, default="Edit",null=True, blank=True,editable=False)
    image = models.ImageField(upload_to="hemophilia/",null=True, blank=True)
    english = HTMLField(null=True, blank=True,)
    hindi = HTMLField(null=True, blank=True)
    created_date =  models.DateTimeField(auto_now_add=True)