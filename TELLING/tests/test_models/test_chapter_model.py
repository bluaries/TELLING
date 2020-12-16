from django.test import TestCase
from TELLING import models
from TELLING.models import Category, Story, Chapter
from django.contrib.auth.models import User


class ChapterModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("User 1", password="pws")
        category = Category.objects.create(category_name="Category 1")
        story = Story.objects.create(
            title="Story 1", author=user,
            categories=category, thumbnail='upload/Grass_Railways.jpg'
        )
        Chapter.objects.create(
            story=story, title_chapter="title")

    def test_chapter_title_max_length(self):
        """
        Test max length of chapter title.
        """
        chapter = Chapter.objects.get(pk=1)
        chapter_title_max_length = chapter._meta.get_field('title_chapter').max_length
        self.assertEquals(chapter_title_max_length, 100)
