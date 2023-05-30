from django.contrib import admin  
from dasboard import views  
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('',views.dasboard),  
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
