from django.contrib import admin
from .models import CustomUser, Alquiler


# Register your models here.

admin.site.register(CustomUser)

admin.site.register(Alquiler)