from django.shortcuts import render,redirect,HttpResponse
from .models import *
from posts.models import NewsCategory,News,Precosan,precosanCategory
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
#======================= Home ===================
def Home(request):
    res = Banner.objects.all().order_by('-created_date')
    res3 = YoutubeVideo.objects.all().order_by('-created_date')
    res4 = News.objects.all().order_by('-created_date')[:4]
    res5 = Precosan.objects.all().order_by('-created_date')[:4]
    about = HistoryHemophilia.objects.get()
    context = {
        'banner_data':res,
        'youtube':res3,
        'hemos_news':res4,
        'presosan':res5,
        'about':about
    }
    return render(request, 'app/home.html',context)

#======================= About ===================
def About(request):
    return render(request, 'about.html')

#======================= About ===================
def History(request):
    about = HistoryHemophilia.objects.get()
    return render(request, 'history.html',{'about':about})

#======================= About ===================
def HemophiliaAbout(request):
    about = AboutHemophilia.objects.get()
    return render(request, 'about-hemophilia.html',{'about':about})


#======================= Contact ===================
def ContactUS(request):
    if request.method == 'POST':
        name = request.POST['name']
        father_name = request.POST['father_name']
        address = request.POST['address']
        adhar_number = request.POST['adhar_number']
        mobile = request.POST['mobile']
        whatsapp_number = request.POST['whatsapp_number']
        email = request.POST['email']
        comment = request.POST['comment']

        contact = Contactus.objects.create(name=name,father_name=father_name,address=address,aadhar_no=adhar_number,mobile=mobile,whatsapp_no=whatsapp_number,email=email,comment=comment)
        contact.save()
        messages.success(request,"Message send successful")
        return redirect('contact-us')
    else:
        return render(request,'contact.html')

#======================= Youtube ===================
def Youtube(request):
    res = YoutubeVideo.objects.all().order_by('-created_date')
    
    paginator = Paginator(res, 15)  # Show 2 objects per page
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    
    context={
        "objects":objects
    }
    return render(request, 'app/youtube.html',context)

#======================= Youtube Details ===================
def YoutubeVideoDetail(request,youtube_slug):
    res1 =  YoutubeVideo.objects.get(slug=youtube_slug)
    res2 = YoutubeVideo.objects.all().order_by('-created_date')[:20] #limit
    context={
        'Youtube_detail':res1,
        'recent_Youtube':res2,
    }
    return render(request,'app/youtube_details.html',context)   


#======================= Team Member ===================
def TeamMember(request):
    res = SocietyCoMember.objects.all().order_by('-created_date')
    context={
        'team_member':res
    }
    return render(request, 'app/team-member.html',context)

def TeamMemberDetail(request,slug):
    team_detail = SocietyCoMember.objects.get(slug=slug)
    context={
        'team_detail':team_detail   
    }
    return render(request, 'app/team-member-detail.html',context)

#======================= Our Doctors ===================
def Doctors(request):
    res = Doctor.objects.all().order_by('-created_date')
    context={
        'hemo_doctor':res
    }
    return render(request, 'app/doctors.html',context)

def DoctorDetail(request, slug):
    dr_detail = Doctor.objects.get(slug=slug)
    context={
        'dr_detail':dr_detail
    }
    return render(request, 'app/doctor-detail.html',context)

