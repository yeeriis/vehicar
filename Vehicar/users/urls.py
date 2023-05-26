from django.urls import path
from .views import registerView, loginView, usuarioView, registerAlquilerView
from . import views
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views



class Protegida(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"content": "Esta vista está protegida"})

urlpatterns = [
    path('register/', registerView.as_view()),
    path('register-leasing/', registerAlquilerView.as_view()),
    path('login/', loginView.as_view()),
    path('usuario/', usuarioView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
