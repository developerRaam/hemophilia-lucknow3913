from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
#======================= Home ===================
def Home(request):
    res = Banner.objects.all().order_by('-created_date')
    #res2 = OurTeam.objects.get()
    res3 = YoutubeVideo.objects.all().order_by('-created_date')
    res4 = News.objects.all().order_by('-created_date')
    context = {
        'banner_data':res,
        #'ourteam':res2,
        'youtube':res3,
        'hemos_news':res4
    }

    return render(request, 'home.html',context)

#======================= About ===================
def About(request):
    return render(request, 'about.html')

#======================= Contact ===================
def ContactUS(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        comment = request.POST['comment']

        contact = Contactus.objects.create(name=name,email=email,mobile=mobile,comment=comment)
        contact.save()
        messages.success(request,"Message send successful")
        return redirect('contact-us')
    else:
        return render(request,'contact.html')

#======================= Youtube ===================
def Youtube(request):
    res = YoutubeVideo.objects.all().order_by('-created_date')
    paginator = Paginator(res, 10) # pagination
    page_number = request.GET.get('page')
    service_data = paginator.get_page(page_number)
    total_page = service_data.paginator.num_pages
    context={
        'youtube_list':service_data,
        'last_page':total_page,
        'total_page_list':[n+1 for n in range(total_page)]
    }
    return render(request, 'youtube.html',context)

#======================= Youtube Details ===================
def YoutubeVideoDetail(request,youtube_slug):
    res1 =  YoutubeVideo.objects.get(slug=youtube_slug)
    res2 = YoutubeVideo.objects.all().order_by('-created_date')[:20] #limit
    context={
        'Youtube_detail':res1,
        'recent_Youtube':res2,
    }
    return render(request,'youtube_details.html',context)   


#======================= Team Member ===================
def TeamMember(request):
    res = SocietyCoMember.objects.all().order_by('-created_date')
    context={
        'team_member':res
    }
    return render(request, 'team-member.html',context)

#======================= Our Doctors ===================
def Doctors(request):
    res = Doctor.objects.all().order_by('-created_date')
    context={
        'hemo_doctor':res
    }
    return render(request, 'doctors.html',context)


#======================= Hemopholia News ===================
def Hemo_News(request):
    res = News.objects.all().order_by('-created_date')
    res2 = News.objects.all().order_by('-views')
    
    paginator = Paginator(res, 15) # pagination
    page_number = request.GET.get('page')
    service_data = paginator.get_page(page_number)
    total_page = service_data.paginator.num_pages

    context={
        'hemo_news':service_data,
        'last_page':total_page,
        'total_page_list':[n+1 for n in range(total_page)],
        'popular_news':res2
    }
    return render(request, 'news.html',context)


#======================= News Details ===================
def NewsDetail(request,title):
    res =  News.objects.get(slug=title)
    res2 = News.objects.all().order_by('-views')
    # views count
    res.views = res.views + 1
    res.save()
    

    context={
        'news_detail':res,
        'popular_news':res2
    }
    return render(request,'news_details.html',context)  

#======================= Precosans ===================
def Precosans(request):
    res = Precosan.objects.all().order_by('-created_date')
    res2 = Precosan.objects.all().order_by('-views')
    
    paginator = Paginator(res, 15) # pagination
    page_number = request.GET.get('page')
    service_data = paginator.get_page(page_number)
    total_page = service_data.paginator.num_pages

    context={
        'precosan_data':service_data,
        'last_page':total_page,
        'total_page_list':[n+1 for n in range(total_page)],
        'popular_precosan':res2
    }
    return render(request, 'precosan.html',context)

#======================= Precosan Detail ===================
def PrecosanDetail(request,title):
    res =  Precosan.objects.get(slug=title)
    res2 = Precosan.objects.all().order_by('-views')
    # views count
    res.views = res.views + 1
    res.save()
    context={
        'precosan_detail':res,
        'popular_precosan':res2,
    }
    return render(request,'precosan_details.html',context)