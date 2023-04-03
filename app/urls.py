from django.urls import path
from django.contrib import admin
from .import views
from registration import views as reg

admin.site.site_header = "Hemophilia Lucknow Admin"
admin.site.site_title = "Hemophilia Lucknow Admin Portal"
admin.site.index_title = "Welcome to Hemophilia Lucknow Researcher Portal"

urlpatterns = [
    path("",views.Home,name="index"),
    path("about-us/",views.About, name="about-us"),
    path("history-of-hemophilia/",views.History),
    path("about-hemophilia-society/",views.HemophiliaAbout),
    
    path("youtube-channel/",views.Youtube, name="youtube-channel"),
    path("youtube/<youtube_slug>/",views.YoutubeVideoDetail, name="youtube"),
    
    path("team-member/",views.TeamMember, name="team-member"),
    path("team-member/<slug>",views.TeamMemberDetail, name="team-member-detail"),
    
    path("doctors/",views.Doctors, name="doctors"),
    path("doctor/<slug>",views.DoctorDetail, name="doctor-detail"),
    
    #Login
    path("login/",reg.Login),
    path("register/",reg.Register),
    
    #Activity post
    path("hemophilia-gallery/",views.HemophiliaGallery),

]