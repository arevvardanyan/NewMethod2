from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from .serializer import *


class ReactView(APIView): 
	
	serializer_class = CategorySerializers 

	def get(self, request): 
		detail = [ {"name": detail.name} 
		for detail in MainCategory.objects.all()] 
		return Response(detail) 

	def post(self, request): 

		serializer = CategorySerializers(data=request.data) 
		if serializer.is_valid(raise_exception=True): 
			serializer.save() 
			return Response(serializer.data) 
