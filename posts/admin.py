from django.contrib import admin
from django.utils.html import format_html
from posts.models import *

# Register your models here.
# New category 
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name","created_date")
admin.site.register(NewsCategory,NewsCategoryAdmin)

# Post news
class NewsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.news_image.url))
    list_display=("news_title","image_tag","news_category","views","post_by","created_date")
admin.site.register(News,NewsAdmin)

# precosan category
class precosanCategoryAdmin(admin.ModelAdmin):
    list_display = ("name","created_date")
admin.site.register(precosanCategory,precosanCategoryAdmin)

#precosan 
class PrecosanAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.pr_image.url))
    list_display=("title","image_tag","category","views","post_by","created_date")
admin.site.register(Precosan,PrecosanAdmin)