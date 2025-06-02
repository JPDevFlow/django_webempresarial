from django.contrib import admin
from .models import category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    list_display = ('title', 'author', 'published')

admin.site.register(category, CategoryAdmin)
admin.site.register(Post, PostAdmin)