from django.contrib import admin
from liker.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'likes', 'dislikes')


admin.site.register(Category, CategoryAdmin)
