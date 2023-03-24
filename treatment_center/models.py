from django.db import models

# Create your models here.
CM_STATUS = ((1, 'Available'), (0, 'Not Available'))

class TreatmentCity(models.Model):
    city_name = models.CharField(max_length=50)
    status = models.SmallIntegerField(choices=CM_STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.city_name
    class Meta:
        verbose_name_plural = "City"
        
class Factor(models.Model):
    factor_name = models.CharField(max_length=100)
    status = models.SmallIntegerField(choices=CM_STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.factor_name
        
class TreatmentCenter(models.Model):
    doctor_name = models.CharField(max_length=50,null=True, blank=True)
    room_no = models.CharField(max_length=50,null=True, blank=True)
    image= models.ImageField(upload_to="treatment_center/", unique=True, null=True, blank=True,)
    hospital_name = models.CharField(max_length=255)
    city = models.ForeignKey(TreatmentCity, verbose_name="City", on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=CM_STATUS, default=1)
    created_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hospital_name
    class Meta:
        verbose_name_plural = "Treatment Center"
        
class SelectMutipleFactor(models.Model):
    treatment_center = models.ForeignKey(TreatmentCenter, on_delete=models.CASCADE)
    factor = models.ForeignKey(Factor, verbose_name="Factor", on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Select Factor'