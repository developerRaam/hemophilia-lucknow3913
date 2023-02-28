from django.contrib import admin
from .models import *

# Register your models here.
class ContactusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    list_display=("name","father_name","aadhar_no","email","mobile","whatsapp_no","address","comment","created_date")
admin.site.register(Contactus,ContactusAdmin)