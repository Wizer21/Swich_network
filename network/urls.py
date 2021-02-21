from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('new_registered', views.new_registered, name = 'new_registered')
]