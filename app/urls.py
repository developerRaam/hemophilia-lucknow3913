from django.urls import path
from django.contrib import admin
from .import views
from posts import views as post
from registration import views as reg


admin.site.site_header = "Hemophilia Lucknow Admin"
admin.site.site_title = "Hemophilia Lucknow Admin Portal"
admin.site.index_title = "Welcome to Hemophilia Lucknow Researcher Portal"

urlpatterns = [
    path("",views.Home,name="index"),
    path("about-us/",views.About, name="about-us"),
    path("history-of-hemophilia/",views.History),
    path("about-hemophilia-society/",views.HemophiliaAbout),
    path("contact-us/",views.ContactUS, name="contact-us"),
    path("youtube-channel/",views.Youtube, name="youtube-channel"),
    path("meet-our-team/",views.TeamMember, name="meet-our-team"),
    path("doctors/",views.Doctors, name="doctors"),
    path("youtube/<youtube_slug>/",views.YoutubeVideoDetail, name="youtube"),
    
    #Posts
    path("news/",post.Hemo_News, name="news"),
    path("news/<title>/",post.NewsDetail, name="news-detail"),
    path("precaution/",post.Precosans, name="precosans"),
    path("precaution/<title>",post.PrecosanDetail, name="precosans-detail"),
    
    #Login
    path("login/",reg.Login),
    path("register/",reg.Register)

]