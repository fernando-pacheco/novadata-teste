from django.contrib import admin
from apps.app.models import Post, Comment

class ListandoPosts(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_per_page = 10

class ListandoComments(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'creation_date')
    list_display_links = ('id', 'author')
    search_fields = ('author', 'content')
    list_per_page = 10

admin.site.register(Post, ListandoPosts)
admin.site.register(Comment, ListandoComments)
