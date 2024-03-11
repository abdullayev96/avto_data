from django.contrib import admin
from .models import Material


class AdminCategory(admin.ModelAdmin):
      list_display = ['id', 'name', 'price','qty' ]

      list_filter = ['id']





admin.site.register(Material, AdminCategory)




