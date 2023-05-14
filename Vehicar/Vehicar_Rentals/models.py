from django.db import models
from django.contrib.auth import authenticate, login

# Create your models here.

COLORES = {
    ('0', 'Blanco'),
    ('1', 'Rojo'),
    ('2', 'Azul'),
    ('3', 'Verde'),
    ('4', 'Amarillo'),
    ('5', 'Negro'),
    ('6', 'Gris'),
    ('7', 'Plata'),
    ('8', 'Granate'),
    ('9', 'Turquesa'),
    ('10', 'Naranja'),
}

PUERTAS = {
    ('0', 'Tres'),
    ('1', 'Cuatro'),
    ('2', 'Cinco'),
}

class Coche(models.Model):
    marca = models.CharField(max_length = 100)
    modelo = models.CharField(max_length = 100)
    matricula = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100 , choices = COLORES)
    puertas = models.CharField(max_length = 100 , choices = PUERTAS)
    tipo_carroceria = models.CharField(max_length = 100)
    anyo = models.CharField(max_length = 100)
    tipo_motor = models.CharField(max_length = 100)
    caballos = models.CharField(max_length = 100)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.modelo

class Persona(models.Model):
    usuario = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    edad = models.IntegerField()
    rol = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)
    coche_propiedad = models.ForeignKey(Coche, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.apellido
        

class Alquiler(models.Model):
    email_usuario = models.ForeignKey(Persona, null=True, on_delete = models.CASCADE)
    coche_alquilado = models.ForeignKey(Coche, null=True, on_delete = models.CASCADE)
    fecha_inicio_alquiler = models.DateField(max_length = 100)
    fecha_fin_alquiler = models.DateField(max_length = 100)
    precio_alquiler = models.IntegerField()

    