from rest_framework import serializers
from .models import *
from category.serializers import *



class ProductSerializer(serializers.ModelSerializer):
   class Meta:
       model = Product
       fields = ['pro_name', 'pro_code']




class MaterialSerializer(serializers.ModelSerializer):
   product_id  = ProductSerializer()
   material_id  = CategorySerializer(many=True)

   class Meta:
       model = ProMaterial
       fields = ['id','product_id', 'quantity', 'material_id',]


