from django.contrib import admin
from .models import category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering =('author', 'published')
    search_fields = ('title','content', 'author__username','categories__name')  # __username para buscar por nombre de usuario del autor, __name para buscar por nombre de la categoría
    date_hierarchy = 'published'  # Permite filtrar por fecha de publicación
    list_filter = ('author__username', 'categories__name')  # Permite filtrar por nombre de autor y nombre de categorías

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])  # Muestra las categorías de la entrada separadas por comas
    post_categories.short_description = 'Categorías'  # Título de la columna en el admin

admin.site.register(category, CategoryAdmin)
admin.site.register(Post, PostAdmin)