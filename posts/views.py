from django.shortcuts import render,redirect,HttpResponse
from posts.models import *
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
#======================= Hemopholia News ===================
def Hemo_News(request):
    res = News.objects.all().order_by('-created_date')
    res2 = News.objects.all().order_by('-created_date')[:7]
    
    paginator = Paginator(res, 15)  # Show 2 objects per page
    page = request.GET.get('page')
    objects = paginator.get_page(page)

    context={
        
        'objects':objects,
        'popular_news':res2
    }
    return render(request, 'posts/news.html',context)

#======================= News Details ===================
def NewsDetail(request,title):
    res =  News.objects.get(slug=title)
    res2 = News.objects.all().order_by('-created_date')[:7]
    # views count
    res.views = res.views + 1
    res.save()
    
    context={
        'news_detail':res,
        'popular_news':res2
    }
    return render(request,'posts/news_details.html',context)  

#======================= Precosans ===================
def Precosans(request):
    res = Precosan.objects.all().order_by('-created_date')
    res2 = Precosan.objects.all().order_by('-created_date')[:7]
    
    paginator = Paginator(res, 15)  # Show 2 objects per page
    page = request.GET.get('page')
    objects = paginator.get_page(page)

    context={
        'objects':objects,
        'popular_precosan':res2
    }
    return render(request,'posts/precosan.html',context)

#======================= Precosan Detail ===================
def PrecosanDetail(request,title):
    res =  Precosan.objects.get(slug=title)
    res2 = Precosan.objects.all().order_by('-created_date')[:7]
    # views count
    res.views = res.views + 1
    res.save()
    context={
        'precosan_detail':res,
        'popular_precosan':res2,
    }
    return render(request,'posts/precosan_details.html',context)