from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('publication', views.publication, name = 'publication'),
    path('logout', views.logout, name = 'logout'),
    path('profile/<int:user_id>', views.profile, name = 'profile'),
    path('profile_edit', views.profile_edit, name = 'profile_edit')
]