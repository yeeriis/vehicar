# Generated by Django 4.2.1 on 2023-05-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicar_Rentals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coche',
            name='precio_alquiler',
            field=models.CharField(default=10, max_length=1000),
            preserve_default=False,
        ),
    ]