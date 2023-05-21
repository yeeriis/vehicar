from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import login


# Create your views here.


class registerView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    

class loginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        return Response({
            'message' : 'success'
        })
        