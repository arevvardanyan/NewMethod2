from .models import *
from rest_framework import serializers



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'