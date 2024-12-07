from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('MabatiApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]