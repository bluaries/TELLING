from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from tinymce import models as tinymce_models

class Category(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

class Story(models.Model):
    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='author')
    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    thumbnail = ResizedImageField(size=[500,300], upload_to = 'image',  blank=True, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Stories"
        
class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title_chapter = models.CharField(max_length = 100)
    content = tinymce_models.HTMLField()
    def __str__(self):
        return self.title_chapter

