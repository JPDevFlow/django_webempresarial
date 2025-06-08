from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def page(reuest, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(reuest, 'pages/sample.html', {'page': page})
  
