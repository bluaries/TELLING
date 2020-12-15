from django.test import TestCase
from django.urls import reverse
from TELLING.models import Story, Category
from django.contrib.auth.models import User


class ShowUserStoryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("User 1", password="pws")
        category = Category.objects.create(category_name="Category 1")
        Story.objects.create(
            title="Story 1", author=self.user,
            categories=category, thumbnail='upload/Grass_Railways.jpg'
        )

    def test_can_access_by_url_name(self):
        """
        Test that a view can be access using url name
        """
        url = reverse('TELLING:show_story')
        self.client.force_login(self.user)

        stories = Story.objects.filter(author=self.user)
        response = self.client.get(url, data={'user_stories': stories})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `user_story.html`
        """
        url = reverse('TELLING:show_story')
        self.client.force_login(self.user)

        stories = Story.objects.filter(author=self.user)
        response = self.client.post(url, data={'user_stories': stories})
        self.assertTemplateUsed(response, 'user_story.html')
