from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    father_name = models.CharField(max_length=50,null=True, blank=True)
    address = models.CharField(max_length=120,null=True, blank=True)
    aadhar_no = models.CharField(max_length=12,null=True, blank=True)
    aadhar_image = models.ImageField(upload_to="contact/",blank=True, null=True)
    mobile = models.BigIntegerField()
    whatsapp_no = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True)
    created_date =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Contact us"