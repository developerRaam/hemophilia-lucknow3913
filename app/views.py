from django.shortcuts import render,redirect,HttpResponse
from .models import *
from posts.models import Posts,Category,ActivityPost
from django.core.paginator import Paginator
from django.contrib import messages
from django.conf import settings

# Create your views here.
#======================= Home ===================
def Home(request):
    res = Banner.objects.all().order_by('-created_date')[:2]
    about = HistoryHemophilia.objects.get()
    activity_post = ActivityPost.objects.all().order_by('-created_date')[:4]
    #Post
    posts = Posts.objects.all().order_by('-created_date')
    category = Category.objects.all()
    data = []
    count = 0
    for cat in category:
        for post in posts:
            if cat.id == post.category_id:
                if count < 4:
                    d = post
                    data.append(d)
                count = count + 1
        count = 0 #reset
    context = {
        'banner_data':res,
        'posts':data,
        'category':category,
        'activity_post':activity_post,
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
    res = SocietyMember.objects.all().order_by('-id')
    context={
        'team_member':res
    }
    return render(request, 'app/team-member.html',context)

def TeamMemberDetail(request,slug):
    team_detail = SocietyMember.objects.get(slug=slug)
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

def HemophiliaGallery(request):
    activity_post = ActivityPost.objects.all().order_by('-created_date')
    paginator = Paginator(activity_post, 20)  # Show 2 objects per page
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, 'hemophilia-gallery.html',{'objects':objects})