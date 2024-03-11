from django.shortcuts import render
from .models import Material
from .serializers import CategorySerializer
from rest_framework.views import APIView, Response
from rest_framework import status


class MaterialAPI(APIView):
     def get(self, request):
              try:
                  cat =  Material.objects.all()
                  serializer = CategorySerializer(cat, many=True)
                  return Response({"result":serializer.data})

              except Exception as a:
                        print(a)

              return Response({"status":status.HTTP_404_NOT_FOUND})


