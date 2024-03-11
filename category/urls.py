from django.urls import path
from .views import MaterialAPI

urlpatterns = [
          path('', MaterialAPI.as_view())
]

###task
###1234..