from django.contrib import admin
from django.urls import path, include
from Vehicar_Rentals.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Vehicar_Rentals.urls')),
    path('coches/<int:id>', CocheDetailView.as_view()),


]