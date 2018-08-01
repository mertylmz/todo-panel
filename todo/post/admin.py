from django.contrib import admin
#from post.models import Post
from .models import Personel, Post



class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']

    class Meta:
        model = Post
admin.site.register(Personel)
admin.site.register(Post, PostAdmin)

