from django.contrib import admin

# Register your models here.
from .models import User, Publication

admin.site.register(User)
admin.site.register(Publication)