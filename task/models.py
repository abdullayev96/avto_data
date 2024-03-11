from django.db import models
from baseapp.models import BaseModel
from category.models import Material




class Product(BaseModel):
     pro_name = models.CharField(max_length=300, verbose_name="Mahsulot nomi:")
     pro_code = models.IntegerField(unique=True)



     def __str__(self):
          return self.pro_name

     class Meta:
          verbose_name = "Mahsulot_nomi_"



class ProMaterial(models.Model):
     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pros_id")
     material_id = models.ManyToManyField(Material, related_name='mat_id')
     quantity = models.IntegerField(verbose_name=" Foydalanilgan xomashyolar soni:")


     class Meta:
          verbose_name = "Xomashyo_Mahsulot_"




# class HouseMaterial(models.Model):
#
#      material_id = models.ManyToManyField(Category, related_name="material_ids")
#      remainder  =  models.IntegerField(verbose_name="Xomashyo qolganini ko’rsatadi:")
#      price  = models.IntegerField(verbose_name="Xomashyo Narx:")
#
#

