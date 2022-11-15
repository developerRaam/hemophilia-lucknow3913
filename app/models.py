from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField #https://django-embed-video.readthedocs.io/en/latest/installation.html


# Create your models here.

CM_STATUS = ((1, 'Enable'), (0, 'Disable'))

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    

class doctorCategory(models.Model):
    name = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class precosanCategory(models.Model):
    name = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class SocietyCoMember(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="co-member/", null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(choices=CM_STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)

class Precosan(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=400,blank=True, null=True)
    category = models.ForeignKey(precosanCategory,null=True, blank=True, on_delete=models.CASCADE, default=1)
    pr_image = models.ImageField(upload_to="precosan/", blank=True, null=True)
    description = HTMLField(null=True, blank=True)
    post_by = models.CharField(max_length=50, default="admin")
    views = models.IntegerField(default="0")
    slug = AutoSlugField(populate_from='title', unique=True,null=True, default=None)
    created_date =  models.DateTimeField(auto_now_add=True)

class YoutubeVideo(models.Model):
    youtube_title = models.CharField(max_length=255)
    youtube_link = EmbedVideoField()
    description = HTMLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='youtube_title', unique=True,null=True, default=None)
    created_date =  models.DateTimeField(auto_now_add=True)

class News(models.Model):
    news_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=400, blank=True, null=True)
    news_image = models.ImageField(upload_to="news/",blank=True, null=True)
    news_category = models.ForeignKey(NewsCategory,null=True, blank=True, on_delete=models.CASCADE, default=1)
    news_description = HTMLField(null=True, blank=True)
    views = models.IntegerField(default="0")
    post_by = models.CharField(max_length=50, default="admin")
    slug = AutoSlugField(populate_from='news_title', unique=True,null=True, default=None)
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
    image = models.ImageField(upload_to="doctors/", null=True, blank=True)
    department = models.ForeignKey(doctorCategory, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=255)
    created_date =  models.DateTimeField(auto_now_add=True)

class OurTeam(models.Model):
    heading = models.CharField(max_length=50)
    caption = models.CharField(max_length=500)
    image = models.ImageField(upload_to="upload/")
    created_date =  models.DateTimeField(auto_now_add=True)

class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    mobile = models.BigIntegerField()
    comment = models.TextField(null=True)
    created_date =  models.DateTimeField(auto_now_add=True)