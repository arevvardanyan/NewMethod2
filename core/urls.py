from django.urls import path
from .views import *

urlpatterns = [
    path('wel/', ReactView.as_view(), name="something"),

 
]