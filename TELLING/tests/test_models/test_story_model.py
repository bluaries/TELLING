from django.test import TestCase
from TELLING import models
from TELLING.models import Author, Category, Story


class StoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(user='Jay')
        category = Category.objects.create(category_name="Love")
        Story.objects.create(author=author, category=category, title="Cars555")

    def test_story_max_length(self):
        """
        Test max length of story.
        """
        story = Story.objects.get(id=1)
        story_max_length = story._meta.get_field('title').max_length
        self.assertEquals(story_max_length, 200)
