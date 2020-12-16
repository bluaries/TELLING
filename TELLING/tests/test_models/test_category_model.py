from django.test import TestCase
from TELLING import models
from TELLING.models import Category, Story
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("User 1", password="pws")
        category = Category.objects.create(category_name="Category 1")
        Story.objects.create(
            title="Story 1", author=user,
            categories=category, thumbnail='upload/Grass_Railways.jpg'
        )

    def test_category_max_length(self):
        """
        Test max length of category.
        """
        category = Category.objects.get(pk=1)
        category_max_length = category._meta.get_field('category_name').max_length
        self.assertEquals(category_max_length, 50)