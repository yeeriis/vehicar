from django.shortcuts import render
from django.http import HttpResponse
from .models import Coche, Persona, Alquiler
from .serializers import CocheSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import json



# Create your views here.

class CocheView(APIView):
    def get(self, request):
        coches = Coche.objects.all()
        data = {'coches':list(coches.values())}
        return JsonResponse(data)
        # serializer = CocheSerializer(coches, many=True)
        # return Response({"Coches": serializer.data})

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
def cargar_imagen(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/gracias/')
    else:
        formulario = MiFormulario()
    return render(request, 'cargar_imagen.html', {'formulario': formulario})

def crear_usuario(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        email = datos.get('email', '')
        password = datos.get('password', '')
        usuario = datos.get('usuario', '')
        nombre = datos.get('nombre', '')
        apellido = datos.get('apellido', '')
        edad = datos.get('edad', '')
        foto = datos.get('foto', '')

        usuario = Persona.objects.create_user(usuario=usuario, email=email, password=password, nombre=nombre, apellido=apellido, edad=edad, foto=foto)
        return JsonResponse({'usuario': usuario.usuario})