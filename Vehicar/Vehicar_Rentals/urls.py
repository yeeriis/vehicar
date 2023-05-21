from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views


urlpatterns = [
    path('coches/', CocheView.as_view()),
    path('coches/<int:id>', CocheDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)