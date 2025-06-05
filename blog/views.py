from django.shortcuts import render, get_object_or_404 #El get_object_or_404 es para obtener un objeto o devolver un error 404 si no existe
from .models import Post, Category
# Create your views here.
#Vistas del blog

def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.get_posts.all()  # Obtiene todas las entradas asociadas a la categoría
    return render(request, "blog/category.html", {'category': category, 'posts': posts})  # Pasa la categoría y las entradas a la plantilla