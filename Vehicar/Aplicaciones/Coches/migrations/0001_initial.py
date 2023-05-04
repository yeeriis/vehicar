# Generated by Django 3.0 on 2023-05-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('8', 'Granate'), ('0', 'Blanco'), ('3', 'Verde'), ('2', 'Azul'), ('1', 'Rojo'), ('9', 'Turquesa'), ('6', 'Gris'), ('7', 'Plata'), ('5', 'Negro'), ('10', 'Naranja'), ('4', 'Amarillo')], max_length=100)),
                ('puertas', models.CharField(choices=[('0', 'Tres'), ('1', 'Cuatro'), ('2', 'Cinco')], max_length=100)),
                ('tipo_carroceria', models.CharField(max_length=100)),
                ('anyo', models.CharField(max_length=100)),
                ('tipo_motor', models.CharField(max_length=100)),
            ],
        ),
    ]
