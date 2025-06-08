from django.urls import path
from . import views

urlpatterns = [
    #paths del pages
    path('<int:page_id>/', views.page, name='page'),   
]
