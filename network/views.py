from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User

user_logged = ""

def home(request):
    return render(request, "network/flux.html", {
        "user": user_logged
    })

def register(request):
    if request.POST.get("user_name"):
        if User.objects.filter(name = request.POST.get("user_name")).exists():
            print("User Already exist")
            return render(request, "network/register.html", {
                "error": "User Already exist"
            })
        else:
            new_user = User(name = request.POST.get("user_name"), code = request.POST.get("password"))
            new_user.save()
            print("User created")
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, "network/register.html")

def login(request):
    global user_logged

    entered_username = request.POST.get("user_name")
    if entered_username:
        # Username entered
        if User.objects.filter(name = entered_username).exists():            
            # Username exists
            user = User.objects.get(name = entered_username)
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