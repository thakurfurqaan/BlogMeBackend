from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Article)

@admin.register(Post)
class PostModel(admin.ModelAdmin):
    list_filter = ('title', 'body')
    list_display = ('title', 'body')