# Generated by Django 3.0 on 2023-05-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coches', '0004_auto_20230502_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coche',
            name='color',
            field=models.CharField(choices=[('1', 'Rojo'), ('9', 'Turquesa'), ('5', 'Negro'), ('7', 'Plata'), ('4', 'Amarillo'), ('3', 'Verde'), ('8', 'Granate'), ('10', 'Naranja'), ('6', 'Gris'), ('0', 'Blanco'), ('2', 'Azul')], max_length=100),
        ),
    ]
