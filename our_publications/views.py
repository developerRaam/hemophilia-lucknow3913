from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def OurPublications(request):
    return render(request, "our_publications/publication.html")