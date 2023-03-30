from django.shortcuts import render
from treatment_center.models import *
from django.core.paginator import Paginator

# Create your views here.
def TreatmentCenterView(request):
    treatment_center = TreatmentCenter.objects.all().order_by('-created_date')
    for_city_counter = TreatmentCenter.objects.all().order_by('-created_date')
    factor = SelectMutipleFactor.objects.all()
    all_factor = Factor.objects.all()
    city = TreatmentCity.objects.all().order_by('city_name')
    
    # Show 2 objects per page
    paginator = Paginator(treatment_center, 15) 
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    
    context={
       'objects':objects,
       'factors':factor,
       'city':city,
       'all_factor':all_factor, 
       'for_city_counter':for_city_counter,
   }
    return render(request, 'treatment_center/treatment-center.html',context)
 
def FilterByCity(request, city_slug,city_id):
    treatment_center = TreatmentCenter.objects.filter(city_id=city_id).order_by('-created_date')
    for_city_counter = TreatmentCenter.objects.all().order_by('-created_date')
    factor = SelectMutipleFactor.objects.all()
    all_factor = Factor.objects.all()
    city = TreatmentCity.objects.all().order_by('city_name')
    context={
       'objects':treatment_center,
       'factors':factor,
       'city':city,
       'all_factor':all_factor, 
       'for_city_counter':for_city_counter
   }
    return render(request, 'treatment_center/filter-by-city.html',context)