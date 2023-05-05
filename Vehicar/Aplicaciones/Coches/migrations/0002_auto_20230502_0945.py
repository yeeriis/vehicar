# Generated by Django 3.0 on 2023-05-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coche',
            name='color',
            field=models.CharField(choices=[('10', 'Naranja'), ('0', 'Blanco'), ('4', 'Amarillo'), ('3', 'Verde'), ('2', 'Azul'), ('5', 'Negro'), ('1', 'Rojo'), ('9', 'Turquesa'), ('8', 'Granate'), ('6', 'Gris'), ('7', 'Plata')], max_length=100),
        ),
        migrations.AlterField(
            model_name='coche',
            name='puertas',
            field=models.CharField(choices=[('2', 'Cinco'), ('1', 'Cuatro'), ('0', 'Tres')], max_length=100),
        ),
    ]