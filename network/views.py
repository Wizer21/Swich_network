from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User

def home(request):
    return render(request, "network/flux.html")

def register(request):    
    return render(request, "network/register.html")

def new_registered(request):
    new_user = User(name = request.POST.get("user_name"), code = request.POST.get("password"))
    new_user.save()

    print(User.objects.all())
    return HttpResponseRedirect(reverse('home'))