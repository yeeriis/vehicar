from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class Persona(models.Model):
    usuario = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    edad = models.IntegerField()
    rol = models.BooleanField(default=False)
    # coche_propiedad = models.ForeignKey(Coche, null=True, on_delete = models.SET_NULL)

