from django.contrib import admin
from .models import Author, Category, Story
from login.models import UserProfileInfo, User

admin.site.register(UserProfileInfo)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Story)

