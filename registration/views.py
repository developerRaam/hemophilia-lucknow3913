from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request, "registration/login.html")

def Register(request):
    return render(request, "registration/register.html")