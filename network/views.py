from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import User, Publication
from django.core.exceptions import ObjectDoesNotExist

user_logged = None

def home(request):
    try:         
        current_user = User.objects.get(us_name = user_logged)
    except ObjectDoesNotExist:
        current_user = None        

    return render(request, "network/flux.html", {
        "user": current_user,
        "publication_list": Publication.objects.all()
    })

def register(request):
    global user_logged

    new_username = request.POST.get("user_name")
    new_password = request.POST.get("password")

    if request.method == "POST":
        # POST request
        if new_username == "":   
            # No username entered              
            return render(request, "network/register.html", {
                "error": "Username not entered"
            })
        elif new_password == "":  
            # No password entered          
            return render(request, "network/register.html", {
                "error": "Password not entered"
            })
        elif User.objects.filter(us_name = new_username).exists():            
            # Already exist
            return render(request, "network/register.html", {
                "error": "Username not avaible"
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
    if request.method == "POST":
        # POST request
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
    size = len(new_text)
    if size > 250:        
        return HttpResponseRedirect(reverse('home'))    
    elif new_text != "":
        current_user = User.objects.get(us_name = user_logged)
        new_post = Publication.objects.create(user_id = current_user.id, user_name = current_user.us_name, text = new_text, date = timezone.now()) 
    
    return HttpResponseRedirect(reverse('home'))     

def logout(request):
    global user_logged
    user_logged = None

    return HttpResponseRedirect(reverse('home')) 

def profile_edit(request):
    if request.method == "POST":
        user = User.objects.get(us_name = user_logged)
        user.us_name = request.POST.get("username")

        return HttpResponseRedirect(reverse('home'))        
    else:
        return render(request, "network/profile_edit.html", {
            "user": User.objects.get(us_name = user_logged)
        })

def profile(request, user_id):
    user_to_display = User.objects.get(id = user_id)

    if user_logged == user_to_display.us_name:
        editable = True
    else:
        editable = False

    return render(request, "network/profile.html", {
        "user": user_to_display,
        "editable": editable,
        "publications": Publication.objects.all()
    })