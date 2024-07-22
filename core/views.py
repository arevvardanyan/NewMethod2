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



class ReactView(APIView):

    def get(self, request):
        category_detail = [{"name": detail.name} for detail in MainCategory.objects.all()]
        company_detail = [{"name": detail.name} for detail in Company.objects.all()]
        product_detail = [
            {"name": detail.name, "description": detail.description, "price_now": detail.price_now, "discount": detail.discount}
            for detail in MainProduct.objects.all()
        ]

        response = {
            'categories': category_detail,
            'companies': company_detail,
            'products': product_detail
        }

        return Response(response)

    def post(self, request):
        data_type = request.data.get('type')
        serializer_class = self.get_serializer_class(data_type)
        
        if not serializer_class:
            return Response({'error': 'Invalid type'}, status=400)
        
        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
    
    def get_serializer_class(self, data_type):
        if data_type == 'category':
            return CategorySerializers
        elif data_type == 'company':
            return CompanySerializers
        elif data_type == 'product':
            return ProductSerializers
        return None