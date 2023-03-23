from django.db import models

# Create your models here.

STATUS = ((1, 'Enable'), (0, 'Disable'))

class OurPublications(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400, null=True, blank=True)
    image = models.ImageField(upload_to="our_publications/image/", max_length=100, blank=True, null=True)
    document = models.FileField(upload_to='our_publications/pdf/',null=True, blank=True)
    document_url = models.CharField(max_length=255,blank=True, null=True)
    document_status = models.SmallIntegerField(choices=STATUS, default=1)
    document_url_status = models.SmallIntegerField(choices=STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Our Publication'
        