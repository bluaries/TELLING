from django.test import TestCase
from TELLING import models
from TELLING.models import Author, Category, Story


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category_name="Love")

    def test_category_max_length(self):
        """
        Test max length of category.
        """
        category = Category.objects.get(id=1)
        category_max_length = category._meta.get_field('category_name').max_length
        self.assertEquals(category_max_length, 200)
