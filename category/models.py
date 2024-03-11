from django.db import models
from baseapp.models import BaseModel




class Material(BaseModel):
      name = models.CharField(max_length=200, verbose_name="Xomashyo nomi:")
      qty = models.IntegerField(verbose_name=" Foydalanilgan xomashyolar soni:")
      price  = models.IntegerField(verbose_name="Xomashyo narxi:")




      def __str__(self):
          return self.name



      class Meta:
          verbose_name = "Xomashyo_"



