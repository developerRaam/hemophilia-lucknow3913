from caption.models import *

# caption field
def SiteProperty(request):
    site = SiteName.objects.get()
    site_name = site.site_heading
    social = Social.objects.get()
    contact = ContactUs.objects.get()
    context = {
        'site_name':site_name,
        'site':site,
        'social':social,
        'contact':contact
    }
    return(context)