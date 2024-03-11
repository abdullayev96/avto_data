from rest_framework import serializers
from .models import Material


class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model = Material
          fields = ['id','name', 'price', 'qty']



