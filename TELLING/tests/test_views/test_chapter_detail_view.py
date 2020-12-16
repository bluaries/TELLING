from django.test import TestCase
from django.urls import reverse
from TELLING.models import Story, Category, Chapter
from django.contrib.auth.models import User


class ChapterDetailTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("User 1", password="pws")
        category = Category.objects.create(category_name="Category 1")
        story = Story.objects.create(
            title="Story 1", author=user,
            categories=category, thumbnail='upload/Grass_Railways.jpg'
        )
        Chapter.objects.create(
            story=story, title_chapter="title")

    def test_can_access_by_url_name(self):
        """
        Test that a view can be access using url name
        """
        url = reverse('TELLING:chapter', kwargs={'pk': 1})

        chapter = Chapter.objects.get(pk=1)
        response = self.client.get(url, data={'chapter': chapter})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `chapter.html`
        """
        url = reverse('TELLING:chapter', kwargs={'pk': 1})

        chapter = Chapter.objects.get(pk=1)
        response = self.client.get(url, data={'chapter': chapter})
        self.assertTemplateUsed(response, 'chapter.html')
