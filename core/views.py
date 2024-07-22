from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from .serializer import *


# class ReactView(APIView): 
	
# 	serializer_class = CategorySerializers 

# 	def get(self, request): 
# 		detail = [ {"name": detail.name} 
# 		for detail in MainCategory.objects.all()] 
# 		return Response(detail) 

# 	def post(self, request): 

# 		serializer = CategorySerializers(data=request.data) 
# 		if serializer.is_valid(raise_exception=True): 
# 			serializer.save() 
# 			return Response(serializer.data) 



class CompanyView(APIView):
    serializer_class = CompanySerializers

    def get(self, request):
        company = [{"name":detail.name} for detail in Company.objects.all()]
        print(company)
        
        return Response(company)


class CategoryView(APIView):
    serializer_class = CategorySerializers

    def get(self, request):
        detail = [{"name": detail.name} for detail in MainCategory.objects.all()]
        
        return Response(detail)


class MainProductView(APIView):
    serializer_class = ProductSerializers

    def get(self, request):
        detail = [{"name": detail.name,"description":detail.description,"img_1":detail.img_1.path} for detail in MainProduct.objects.all()]
        
        return Response(detail)
