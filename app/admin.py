from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.

#doctor category
class doctorCategoryAdmin(admin.ModelAdmin):
    list_display = ("name","created_date")
admin.site.register(doctorCategory,doctorCategoryAdmin)


#society member
class SocietyCoMemberAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("name","image_tag","position","status","created_date")
admin.site.register(SocietyCoMember,SocietyCoMemberAdmin)

# Youtube link
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display=("youtube_title","youtube_link","created_date")
admin.site.register(YoutubeVideo,YoutubeVideoAdmin)

# Set banner on the front side
class BannerAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.banner_img.url))

    list_display=("image_tag","heading","sub_heading","link","link_text","status","created_date")
admin.site.register(Banner,BannerAdmin)

# Add doctor list
class DoctorAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("name","image_tag","department","mobile","description","created_date")
admin.site.register(Doctor,DoctorAdmin)

class ContactusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    list_display=("name","father_name","aadhar_no","email","mobile","whatsapp_no","address","comment","created_date")
admin.site.register(Contactus,ContactusAdmin)

class AboutHemophiliaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ("edit",)
admin.site.register(AboutHemophilia,AboutHemophiliaAdmin)

class HistoryHemophiliaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ("edit",)
admin.site.register(HistoryHemophilia,HistoryHemophiliaAdmin)