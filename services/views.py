from django.shortcuts import render

# Create your views here.
def services(req):
    context={'profile':'active'}
    return render(req,'services/services.html',context)
