from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
class precosanCategory(models.Model):
    name = models.CharField(max_length=50)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Precosan(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=400,blank=True, null=True)
    category = models.ForeignKey(precosanCategory,null=True, blank=True, on_delete=models.CASCADE, default=1)
    pr_image = models.ImageField(upload_to="precosan/", blank=True, null=True)
    english_description = HTMLField(null=True, blank=True,)
    hindi_description = HTMLField(null=True, blank=True)
    post_by = models.CharField(max_length=50, default="admin")
    views = models.IntegerField(default="0", editable=None)
    slug = AutoSlugField(max_length=255,populate_from='title', unique=True,null=True, default=None,always_update=True)
    created_date =  models.DateTimeField(auto_now_add=True)
    
class News(models.Model):
    news_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=400, blank=True, null=True)
    news_image = models.ImageField(upload_to="news/",blank=True, null=True)
    news_category = models.ForeignKey(NewsCategory,null=True, blank=True, on_delete=models.CASCADE, default=1)
    english_description = HTMLField(null=True, blank=True)
    hindi_description = HTMLField(null=True, blank=True)
    views = models.IntegerField(default="0", editable=None)
    post_by = models.CharField(max_length=50, default="admin")
    slug = AutoSlugField(max_length=255,populate_from='news_title', unique=True,null=True, default=None,always_update=True)
    created_date =  models.DateTimeField(auto_now_add=True)