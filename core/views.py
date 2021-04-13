from django.shortcuts import render
from .models import Contact
# Create your views here.

def home(request):
    context={'home':'active'}
    return render(request,'core/home.html',context)

def contact(req):
    if(req.method=='POST'):
        name=req.POST.get('name')
        email=req.POST.get('email')
        subject=req.POST.get('subject')
        msg=req.POST.get('msg')
        c=Contact.objects.create(name=name,email=email,subject=subject,message=msg)
        
        
    context={'contact':'active'}
    return render(req,'core/contact.html',context)