from django.db import models
from django.contrib.auth import authenticate, login

# Create your models here.

class Coche(models.Model):
    marca = models.CharField(max_length = 100)
    modelo = models.CharField(max_length = 100)
    matricula = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    puertas = models.CharField(max_length = 100)
    tipo_carroceria = models.CharField(max_length = 100)
    anyo = models.CharField(max_length = 100)
    tipo_motor = models.CharField(max_length = 100)
    caballos = models.CharField(max_length = 100)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)
    precio_alquiler = models.CharField(max_length=1000)

    def __str__(self):
        return self.modelo
        


    