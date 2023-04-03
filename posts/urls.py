from django.urls import path
from .import views

urlpatterns = [
    path("c/<cat_slug>",views.Post, name="post"),
    path("<title>/",views.PostDetail, name="post-detail"),
]