from rest_framework import serializers
from Vehicar_Rentals.models import *

class CocheSerializer(serializers.Serializer):
    class Meta:
        model = Coche
        fields = '__all__'
    # marca = serializers.CharField(max_length = 100)
    # modelo = serializers.CharField(max_length = 100)
    # matricula = serializers.CharField(max_length = 100)
    # color = serializers.CharField(max_length = 100)
    # puertas = serializers.CharField(max_length = 100)
    # tipo_carroceria = serializers.CharField(max_length = 100)
    # anyo = serializers.CharField(max_length = 100)
    # tipo_motor = serializers.CharField(max_length = 100)

class CocheDetailSerializer(serializers.Serializer):
    class Meta:
        model = Coche
        fields = '__all__'