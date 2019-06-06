from django.contrib import admin
from django.urls import path, include

from homepage.views import start_BG_process

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  
]


start_BG_process()
