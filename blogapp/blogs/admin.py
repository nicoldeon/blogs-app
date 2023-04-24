from django.contrib import admin
from .models import Blog, Category, User


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'likes']
    search_fields = ['title']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username']


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(User, UserAdmin)
