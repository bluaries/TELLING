from django.contrib import admin
from .models import Category, Story, Chapter

admin.site.register(Story)
admin.site.register(Category)
admin.site.register(Chapter)