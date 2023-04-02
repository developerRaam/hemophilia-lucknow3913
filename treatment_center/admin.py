from django.contrib import admin
from treatment_center.models import *
from django.utils.html import format_html

# Register your models here.
class TreatmentCityAdmin(admin.ModelAdmin):
    list_display = ("city_name","status","created_date")
admin.site.register(TreatmentCity,TreatmentCityAdmin)

class FactorAdmin(admin.ModelAdmin):
    list_display = ("factor_name","status","created_date")
admin.site.register(Factor,FactorAdmin)

class SelectMutipleFactorInline(admin.StackedInline):
    model = SelectMutipleFactor
class TreatmentCenterAdmin(admin.ModelAdmin):
    inlines = [SelectMutipleFactorInline] # Select multiple
    SelectMutipleFactorInline.extra = 1 # Extra option
    list_display = ("hospital_name","city","created_date")
admin.site.register(TreatmentCenter,TreatmentCenterAdmin)

class UploadMapAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display = ("image_tag",)
admin.site.register(UploadMap,UploadMapAdmin)