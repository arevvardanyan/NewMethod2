from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name="category"),
    path('company/',CompanyView.as_view(),name='company'),
    path('mainproduct/',MainProductView.as_view(),name='mainproduct'),
 
]