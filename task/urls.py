from django.urls import path
from .views import ProductMaterialAPI, ProductAPI



urlpatterns = [
        path('', ProductMaterialAPI.as_view()),
        path('pro/', ProductAPI.as_view())
]