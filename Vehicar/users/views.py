from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, AlquilerSerializer
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer
import json


# Create your views here.


class registerView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    

class loginView(APIView):
    def post(self,  request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()
        data = {}
        data['usuario'] = user.usuario
        data['nombre'] = user.nombre
        data['email'] = user.email
        data['edad'] = user.edad
        data['apellido'] = user.apellido
        # data['foto'] = user.foto

 
        json_data = json.dumps(data)

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        return Response( json_data )
    
    def get(self, request, format=None):
        email = request.data['email']

        users = CustomUser.objects.filter(email = email).first()
        serializer = MyTokenObtainPairSerializer(users, many=True)
        return Response(serializer.data)
    
class registerAlquilerView(APIView):
    def post(self, request):
        serializer = AlquilerSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
        
class usuarioView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']



class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)  # Permitir acceso a todos los usuarios
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            refresh_token = response.data['refresh']
            access_token = response.data['access']
            # decoded_access_token = RefreshToken(access_token).payload

            # Imprimir el token en la consola
            print(f"Access Token: {access_token}")
            print(f"Refresh Token: {refresh_token}")

            # Otra opción: incluir el token en la respuesta HTTP
            # response.data['access_token'] = access_token
            # response.data['refresh_token'] = refresh_token

        return response

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)  # Permitir acceso a todos los usuarios