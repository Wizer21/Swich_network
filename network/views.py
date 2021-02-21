from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


from .models import User, Publication

user_logged = ""

def home(request):
    User.objects.all().delete()
    Publication.objects.all().delete()
    return render(request, "network/flux.html", {
        "user": user_logged,
        "publication_list": Publication.objects.all()
    })

def register(request):
    if request.POST.get("user_name"):
        if User.objects.filter(us_name = request.POST.get("user_name")).exists():
            return render(request, "network/register.html", {
                "error": "User Already exist"
            })
        else:
            new_user = User(us_name = request.POST.get("user_name"), us_password = request.POST.get("password"))
            new_user.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, "network/register.html")

def login(request):
    global user_logged

    entered_username = request.POST.get("user_name")
    if entered_username:
        # Username entered
        if User.objects.filter(us_name = entered_username).exists():            
            # Username exists
            user = User.objects.get(us_name = entered_username)
            if request.POST.get("password") == str(user.code):  
                # Password valid
                user_logged = entered_username
                return HttpResponseRedirect(reverse('home'))              
        # Password or Username incorrect
        return render(request, "network/login.html", {
            "error": "Unknow password or username",
            "user_name": request.POST.get("user_name"),
            "password": request.POST.get("password")
        })
    else:
        return render(request, "network/login.html")
    
def publication(request):
    new_text = request.POST.get("publication_text")
    if new_text != "":
        current_user = User.objects.get(us_name = user_logged)
        new_post = Publication(user_id = current_user.id, user_name = current_user.name, text = new_text) 
        new_post.save()
    
    return HttpResponseRedirect(reverse('home'))     