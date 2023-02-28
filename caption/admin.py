from django.contrib import admin
from .models import *

# Register your models here.
class SiteNameAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ("edit","site_heading","image","site_desc",)
admin.site.register(SiteName,SiteNameAdmin)

class SocialAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ("edit","facebook","instagram","youtube","twitter")
admin.site.register(Social,SocialAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ("edit","address","contact1","contact2","email1","email2")
admin.site.register(ContactUs,ContactUsAdmin)