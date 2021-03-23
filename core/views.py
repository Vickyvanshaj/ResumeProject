from django.shortcuts import render
from .models import Contact
# Create your views here.

def home(request):
    context={'home':'active'}
    return render(request,'core/home.html',context)

def contact(req):
    if(req.method=='POST'):
        c=Contact(req.POST)
        
    context={'contact':'active'}
    return render(req,'core/contact.html',context)