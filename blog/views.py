from django.shortcuts import render, get_object_or_404 #El get_object_or_404 es para obtener un objeto o devolver un error 404 si no existe
from .models import Post, category
# Create your views here.
#Vistas del blog

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})


def category(request, category_id):
    category = get_object_or_404(category, id=category_id)
    return render(request, "blog/category.html", {"category": category})