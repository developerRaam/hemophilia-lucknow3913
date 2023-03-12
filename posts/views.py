from django.shortcuts import render,redirect,HttpResponse
from posts.models import *
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
#======================= Hemopholia post ===================
def Post(request,cat_slug):
    res2 = Posts.objects.all().order_by('-created_date')[:7]
    cat = Category.objects.get(slug=cat_slug)
    filter_cat = Posts.objects.filter(category=cat.id).order_by('-created_date')
    
    paginator = Paginator(filter_cat, 15)  # Show 2 objects per page
    page = request.GET.get('page')
    objects = paginator.get_page(page)

    context={
        'cat_name':cat.name,
        'objects':objects,
        'popular_post':res2
    }
    return render(request, 'posts/post.html',context)

#======================= post Details ===================
def PostDetail(request,title):
    res =  Posts.objects.get(slug=title)
    res2 = Posts.objects.all().order_by('-created_date')[:7]
    # views count
    res.views = res.views + 1
    res.save()
    
    context={
        'post_detail':res,
        'popular_post':res2
    }
    return render(request,'posts/post_details.html',context)  


# def Articles(request):
#     article_one = Article.objects.get()
#     article_all = Article.objects.all()
    