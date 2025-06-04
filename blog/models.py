from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User# este es el modelo de usuario por defecto de Django

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to='blog', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)#El models.CASCADE significa que si se elimina el usuario, se eliminarán también sus entradas
    categories =models.ManyToManyField(category, verbose_name="Categorías", related_name="get_posts") # ManyToManyField permite que una entrada tenga varias categorías y una categoría tenga varias entradas
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']
    def __str__(self):
        return self.title