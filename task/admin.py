from django.contrib import admin
from .models import *



class AdminProduct(admin.ModelAdmin):
      list_display = ['id', 'pro_name', 'pro_code']

      list_filter = ['id', 'pro_name']





admin.site.register(Product, AdminProduct)
admin.site.register(ProMaterial)


