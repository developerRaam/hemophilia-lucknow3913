from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=50,populate_from='name', unique=True,null=True,blank=True, default=None,always_update=True)
    created_date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Category'
    
class Posts(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=400,blank=True, null=True)
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="post_image/", blank=True, null=True)
    english_description = HTMLField(null=True, blank=True,)
    hindi_description = HTMLField(null=True, blank=True)
    post_by = models.CharField(max_length=50, default="admin")
    views = models.IntegerField(default="0", editable=None)
    slug = AutoSlugField(max_length=255,populate_from='title', unique=True,null=True, default=None,always_update=True)
    created_date =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Post'
    
class ActivityPost(models.Model):
    title = models.CharField(max_length=250,blank=True, null=True)
    image = models.ImageField(upload_to="activity_post/",blank=True, null=True)
    post_by = models.CharField(max_length=50, default="admin", editable=False)
    created_date =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Activity Post'
    