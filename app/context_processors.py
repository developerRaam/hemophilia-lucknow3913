from caption.models import *
from posts.models import Category

# caption field
def SiteProperty(request):
    site = SiteName.objects.get()
    site_name = site.site_heading
    social = Social.objects.get()
    contact = ContactUs.objects.get()
    #Post category
    post_cat = Category.objects.all().order_by('-created_date')
    context = {
        'site_name':site_name,
        'site':site,
        'social':social,
        'contact':contact,
        'post_cat':post_cat
    }
    return(context)