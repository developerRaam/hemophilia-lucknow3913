from django.contrib import admin
from our_publications.models import *
from django.utils.html import format_html

# Register your models here.
class OurPublicationsAdmin(admin.ModelAdmin):
    def images(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:70px; max-height:70px"/>'.format(obj.image.url))
    list_display=("title","images","document","document_url","document_status","document_url_status","created_date",)
admin.site.register(OurPublications,OurPublicationsAdmin)