from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.

# New category 
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name","created_date")
admin.site.register(NewsCategory,NewsCategoryAdmin)

#doctor category
class doctorCategoryAdmin(admin.ModelAdmin):
    list_display = ("name","created_date")
admin.site.register(doctorCategory,doctorCategoryAdmin)

# precosan category
class precosanCategoryAdmin(admin.ModelAdmin):
    list_display = ("name","created_date")
admin.site.register(precosanCategory,precosanCategoryAdmin)

#society member
class SocietyCoMemberAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("name","image_tag","position","status","created_date")
admin.site.register(SocietyCoMember,SocietyCoMemberAdmin)

#precosan 
class PrecosanAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.pr_image.url))
    list_display=("title","image_tag","category","views","post_by","created_date")
admin.site.register(Precosan,PrecosanAdmin)

# Youtube link
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display=("youtube_title","youtube_link","created_date")
admin.site.register(YoutubeVideo,YoutubeVideoAdmin)

# Post news
class NewsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.news_image.url))
    list_display=("news_title","image_tag","news_category","views","post_by","created_date")
admin.site.register(News,NewsAdmin)

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

# Team member
class OurTeamAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))

    list_display=("image_tag","heading","caption")
admin.site.register(OurTeam,OurTeamAdmin)

class ContactusAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","comment","created_date")
admin.site.register(Contactus,ContactusAdmin)
