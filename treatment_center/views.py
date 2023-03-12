from django.shortcuts import render

# Create your views here.
def TreatmentCenter(request):
    return render(request, 'treatment_center/treatment-center.html')