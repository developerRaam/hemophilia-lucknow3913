from django.shortcuts import render,redirect,HttpResponse
from .models import *

# Create your views here.
def OurPublication(request):
    publication = OurPublications.objects.all().order_by('-created_date')
    context = {
        'publication':publication
    }
    return render(request, "our_publications/publication.html",context)