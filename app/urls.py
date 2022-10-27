from django.urls import path
from django.contrib import admin
from .import views


admin.site.site_header = "Hemophilia Lucknow Admin"
admin.site.site_title = "Hemophilia Lucknow Admin Portal"
admin.site.index_title = "Welcome to Hemophilia Lucknow Researcher Portal"

urlpatterns = [
    path("",views.Home,name="index"),
    path("about-us/",views.About, name="about-us"),
    path("contact-us/",views.ContactUS, name="contact-us"),
    path("youtube-channel/",views.Youtube, name="youtube-channel"),
    path("meet-our-team/",views.TeamMember, name="meet-our-team"),
    path("doctors/",views.Doctors, name="doctors"),
    path("news/",views.Hemo_News, name="news"),
    path("news/<title>/",views.NewsDetail, name="news-detail"),
    path("youtube/<youtube_slug>/",views.YoutubeVideoDetail, name="youtube"),
    path("precosans/",views.Precosans, name="precosans"),
    path("precosans/<title>",views.PrecosanDetail, name="precosans-detail"),

]