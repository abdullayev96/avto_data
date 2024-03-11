from django.shortcuts import render
from  rest_framework.views import APIView, Response
from rest_framework import status
from .serializers import *
from .models import *



class ProductAPI(APIView):
     def get(self, request):
          try:
              pro = Product.objects.all()
              serializers  = ProductSerializer(pro, many=True)
              return Response({"product":serializers.data})


          except Exception as a:
                    print(a)

          return Response({"status":status.HTTP_404_NOT_FOUND})


class ProductMaterialAPI(APIView):
     def get(self, request):
          try:
              mat = ProMaterial.objects.all()
              serializers = MaterialSerializer(mat, many=True)
              return Response({"result":serializers.data})

          except Exception as e:
                    print(e)

          return Response({"status":status.HTTP_404_NOT_FOUND})

