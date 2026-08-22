from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # avisa ao projeto principal que as rotas website estão definidas no arquivo website/urls.py:
    path('', include('website.urls')), 
]