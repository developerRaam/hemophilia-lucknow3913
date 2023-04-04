from django.contrib import admin
from django.utils.html import format_html
from posts.models import *

# Register your models here.
#category
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name","slug","created_date")
# admin.site.register(Category,CategoryAdmin)

#post
class PostsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("title","category","views","post_by","created_date")
admin.site.register(Posts,PostsAdmin)

#ActivityPost
class SelectMutipleActivityPostInline(admin.StackedInline):
    model = SelectMutipleActivityPost
class ActivityPostAdmin(admin.ModelAdmin):
    inlines = [SelectMutipleActivityPostInline] # Select multiple
    SelectMutipleActivityPostInline.extra = 1 # Extra option
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("title","image_tag","created_date")
admin.site.register(ActivityPost,ActivityPostAdmin)
