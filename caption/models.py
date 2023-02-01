from django.db import models

# Create your models here.
class SiteName(models.Model):
    edit = models.CharField(max_length=50, default="Edit",null=True, blank=True,editable=False)
    site_heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to="site_image/", null=True,blank=True)
    site_desc = models.CharField(max_length=500, blank=True,null=True)
    on_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.site_heading
    
    
class Social(models.Model):
    edit = models.CharField(max_length=50, default="Edit",null=True, blank=True,editable=False)
    facebook = models.CharField(max_length=250,blank=True,null=True)
    facebook_group = models.CharField(max_length=250,blank=True,null=True)
    instagram = models.CharField(max_length=250,blank=True,null=True)
    youtube = models.CharField(max_length=250,blank=True,null=True)
    twitter = models.CharField(max_length=250,blank=True,null=True)
    on_date = models.DateTimeField(auto_now_add=True)
    
class ContactUs(models.Model):
    edit = models.CharField(max_length=50, default="Edit",null=True, blank=True,editable=False)
    address = models.CharField(max_length=300,blank=True,null=True)
    contact1 = models.CharField(verbose_name="Contact", max_length=20,blank=True,null=True)
    contact2 = models.CharField(verbose_name="Alternate Contact",max_length=20,blank=True,null=True)
    email1 = models.CharField(verbose_name="Email", max_length=40,blank=True,null=True)
    email2 = models.CharField(verbose_name="Alternate Email", max_length=40,blank=True,null=True)
    on_date = models.DateTimeField(auto_now_add=True)
    