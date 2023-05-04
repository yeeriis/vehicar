from django.db import models

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