from django.contrib import admin
from .models import Coche, Persona, Alquiler

# Register your models here.

admin.site.register(Coche)

admin.site.register(Persona)

admin.site.register(Alquiler)