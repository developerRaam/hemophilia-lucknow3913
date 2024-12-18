from django.shortcuts import render
from contact.models import *
from django.contrib import messages
from mimetypes import MimeTypes
from django.conf import settings
# for email send
from django.core.mail import send_mail,EmailMultiAlternatives
# send html page in email
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

#======================= start Contact ===================
def ContactUS(request):
    if request.method == 'POST':
        name = request.POST['name']
        father_name = request.POST['father_name']
        address = request.POST['address']
        aadhar_number = request.POST['adhar_number']
        aadhar_image = request.FILES['aadhar_image']
        mobile = request.POST['mobile']
        whatsapp_number = request.POST['whatsapp_number']
        email = request.POST['email']
        comment = request.POST['comment']
        
        size = aadhar_image.size # check file size
        type = MimeTypes().guess_type(str(aadhar_image))[0] #check file type
        if type == 'image/png' or type == 'image/jpg' or type == 'image/jpeg' :
            if size <= 5242931: # check of image < 5MB
                contact = Contactus.objects.create(name=name,father_name=father_name,address=address,aadhar_no=aadhar_number,aadhar_image=aadhar_image,mobile=mobile,whatsapp_no=whatsapp_number,email=email,comment=comment)
                contact.save()
                send_mail_after_submit(name,father_name,aadhar_number,mobile,whatsapp_number,email,address,comment)
                messages.success(request,"Message send successful")
                return render(request,'contact/contact.html')
            else:
                return render(request, "contact/contact.html",{'error':'Please upload image only less than 5MB'})
        else:
            return render(request, "contact/contact.html",{'error':'Please choose PNG, JPG, JPEG file'})
    else:
        return render(request,'contact/contact.html')
    
#============ send mail ====================
def send_mail_after_submit(name,father_name,aadhar_number,mobile,whatsapp_number,email,address,comment):
    context={
        'name':name,
        'father_name':father_name,
        'aadhar_number':aadhar_number,
        'mobile':mobile,
        'whatsapp_number':whatsapp_number,
        'email':email,
        'address':address,
        'comment':comment,
    }
    html_content = render_to_string("contact/email_template.html",context)#render html template
    text_content = strip_tags(html_content) #remove html and send text only
    email = EmailMultiAlternatives(
        'New patient message!',
        text_content,
        settings.EMAIL_HOST_USER,
        ['hemophilialucknow2020@gmail.com']   
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
    
#======================= end Contact ===================
