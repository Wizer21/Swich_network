from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


from .models import User, Publication

user_logged = ""

def home(request):
    return render(request, "network/flux.html", {
        "user": user_logged,
        "publication_list": Publication.objects.all()
    })

def register(request):
    global user_logged

    new_username = request.POST.get("user_name")
    if new_username:
        # Username entered

        if User.objects.filter(us_name = new_username).exists():            
            # Already exist
            return render(request, "network/register.html", {
                "error": "User Already exist"
            })
        else:    
            # Username free to use
            new_user = User(us_name = new_username, us_password = request.POST.get("password"))
            new_user.save()

            user_logged = new_username
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
            if request.POST.get("password") == str(user.us_password):  
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
        new_post = Publication.objects.create(user_id = current_user.id, user_name = current_user.us_name, text = new_text, date = timezone.now()) 
    
    return HttpResponseRedirect(reverse('home'))     