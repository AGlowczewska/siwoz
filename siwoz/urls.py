from django.contrib import admin
from django.urls import path
from django.urls import include
from web_registry.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_registry.urls')),
]
