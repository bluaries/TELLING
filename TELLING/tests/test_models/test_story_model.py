from django.test import TestCase
from TELLING import models
from TELLING.models import Category, Story
from django.contrib.auth.models import User


class StoryModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("User 1", password="pws")
        category = Category.objects.create(category_name="Category 1")
        Story.objects.create(
            title="Story 1", author=user,
            categories=category, thumbnail='upload/Grass_Railways.jpg'
        )

    def test_story_max_length(self):
        """
        Test max length of story.
        """
        story = Story.objects.get(pk=1)
        story_max_length = story._meta.get_field('title').max_length
        self.assertEquals(story_max_length, 100)
