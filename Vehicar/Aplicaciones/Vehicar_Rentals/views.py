from django.shortcuts import render
from django.http import HttpResponse
from .models import Coche, Persona, Alquiler
from django.http import JsonResponse


# Create your views here.

def home(request):
    queryset = Coche.objects.all()
    data = list(queryset.values()) # Convierte los resultados de la query en una lista de diccionarios
    return JsonResponse(data, safe=False)