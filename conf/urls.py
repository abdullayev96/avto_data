from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cat/', include('category.urls')),
    path('api/task/', include('task.urls'))
]



#####  task1
####1234..