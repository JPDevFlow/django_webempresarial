from django.shortcuts import render
from .models import Post
# Create your views here.
#Vistas del blog

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})