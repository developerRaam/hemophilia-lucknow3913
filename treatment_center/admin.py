from django.contrib import admin
from treatment_center.models import *

# Register your models here.
class TreatmentCityAdmin(admin.ModelAdmin):
    list_display = ("city_name","slug","status","created_date")
admin.site.register(TreatmentCity,TreatmentCityAdmin)

class FactorAdmin(admin.ModelAdmin):
    list_display = ("factor_name","status","created_date")
admin.site.register(Factor,FactorAdmin)

class SelectMutipleFactorInline(admin.StackedInline):
    model = SelectMutipleFactor
class TreatmentCenterAdmin(admin.ModelAdmin):
    inlines = [SelectMutipleFactorInline] # Select multiple
    SelectMutipleFactorInline.extra = 1 # Extra option
    list_display = ("hospital_name","room_no","created_date")
admin.site.register(TreatmentCenter,TreatmentCenterAdmin)