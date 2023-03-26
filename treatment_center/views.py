from django.shortcuts import render
from treatment_center.models import *

# Create your views here.
def TreatmentCenterView(request):
    treatment_center = TreatmentCenter.objects.all().order_by('-created_date')
    factor = SelectMutipleFactor.objects.all()
    all_factor = Factor.objects.all()
    city = TreatmentCity.objects.all().order_by('city_name')
    context={
       'treatment_center':treatment_center,
       'factors':factor,
       'city':city,
       'all_factor':all_factor, 
   }
    return render(request, 'treatment_center/treatment-center.html',context)
 
def FilterByCity(request, city_slug,city_id):
    treatment_center = TreatmentCenter.objects.filter(city_id=city_id).order_by('-created_date')
    factor = SelectMutipleFactor.objects.all()
    all_factor = Factor.objects.all()
    city = TreatmentCity.objects.all().order_by('city_name')
    context={
       'treatment_center':treatment_center,
       'factors':factor,
       'city':city,
       'all_factor':all_factor, 
   }
    return render(request, 'treatment_center/filter-by-city.html',context)