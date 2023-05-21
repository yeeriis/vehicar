from django.shortcuts import render
from django.http import HttpResponse
from .models import Coche
from .serializers import CocheSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

class CocheView(APIView):
    def get(self, request):
        coches = Coche.objects.all()
        data = {'coches':list(coches.values())}
        return JsonResponse(data)
        # serializer = CocheSerializer(coches, many=True)
        # return Response({"Coches": serializer.data})

class CocheDetailView(APIView):
    def get(self, request, id):
        coches = Coche.objects.filter(id=id)
        data = {'coches':list(coches.values())}
        return JsonResponse(data)
    

def cargar_imagen(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/gracias/')
    else:
        formulario = MiFormulario()
    return render(request, 'cargar_imagen.html', {'formulario': formulario})


