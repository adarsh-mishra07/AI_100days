from django.urls import path
from . import views
from .models import Prediction
urlpatterns = [
    path('', views.home, name='home'),
]