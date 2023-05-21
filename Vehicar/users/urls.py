from django.urls import path
from .views import registerView, loginView
from . import views

urlpatterns = [
    path('register/', registerView.as_view()),
    path('login/', loginView.as_view()),
]
