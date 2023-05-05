# Generated by Django 3.0 on 2023-05-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coches', '0005_auto_20230502_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coche',
            name='color',
            field=models.CharField(choices=[('0', 'Blanco'), ('3', 'Verde'), ('1', 'Rojo'), ('6', 'Gris'), ('7', 'Plata'), ('10', 'Naranja'), ('9', 'Turquesa'), ('5', 'Negro'), ('8', 'Granate'), ('2', 'Azul'), ('4', 'Amarillo')], max_length=100),
        ),
        migrations.AlterField(
            model_name='coche',
            name='puertas',
            field=models.CharField(choices=[('2', 'Cinco'), ('0', 'Tres'), ('1', 'Cuatro')], max_length=100),
        ),
    ]