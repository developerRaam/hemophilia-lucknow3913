from django.urls import path
from .import views

urlpatterns = [
    path("",views.TreatmentCenterView),
    path("<city_id>/<city_slug>/",views.FilterByCity, name="city")

]