from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from Vehicar_Rentals.models import Coche
from django.contrib.auth.hashers import make_password


# Create your models here.



class CustomUserManager(BaseUserManager):
    def CreateUser(self, nombre, apellido, edad, foto, usuario, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # def save(self, *args, **kwargs):
        user.set_password(password)
            # super().save(*args, **kwargs
        user.set_nombre(nombre)
        user.set_apellido(apellido)
        user.set_edad(edad)
        user.set_foto(foto)
        user.set_usuario(usuario)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length = 100, unique=True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    edad = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)
    coche_propiedad = models.ForeignKey(Coche, null=True, on_delete = models.CASCADE, blank=True)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'email', 'password', 'edad', 'foto']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Alquiler(models.Model):
    email_usuario = models.ForeignKey(CustomUser, null=True, on_delete = models.CASCADE)
    coche_alquilado = models.ForeignKey(Coche, null=True, on_delete = models.CASCADE)
    fecha_inicio_alquiler = models.DateField(max_length = 100)
    fecha_fin_alquiler = models.DateField(max_length = 100)
    precio_alquiler = models.CharField(max_length=1000, default= 10)

    def __str__(self):
        return self.email_usuario