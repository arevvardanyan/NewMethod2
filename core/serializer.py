from .models import *
from rest_framework import serializers



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        models = Company
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        models = MainProduct
        fields = ['name','description','img_1','img_2','img_3','category','price_now','discount']