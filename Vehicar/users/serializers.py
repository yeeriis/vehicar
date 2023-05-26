from rest_framework import serializers
from .models import CustomUser, Alquiler
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['usuario', 'nombre', 'apellido', 'email', 'password', 'edad', 'foto' ]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class AlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = ['email_usuario', 'coche_alquilado', 'fecha_inicio_alquiler', 'fecha_fin_alquiler', 'precio_alquiler']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Puedes agregar lógica adicional aquí si es necesario
        return data