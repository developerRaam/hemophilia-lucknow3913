from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("image_tag","image","created_date")
admin.site.register(Gallery,GalleryAdmin)