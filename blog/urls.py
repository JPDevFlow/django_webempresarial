from django.urls import path
from . import views

urlpatterns = [
    #paths del blog
    
    path('', views.blog, name='blog'),
  
    
]
