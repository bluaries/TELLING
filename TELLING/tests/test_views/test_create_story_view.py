from django.test import TestCase
from django.urls import reverse
from TELLING.models import Story, Category
from TELLING.forms import StoryForm
from django.contrib.auth.models import User


class CreateStoryTest(TestCase):
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
        self.client.force_login(self.user)
        url = reverse('TELLING:create_story')
        response = self.client.get(url, data={'story_form': StoryForm()})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `create_story.html`
        """
        self.client.force_login(self.user)
        url = reverse('TELLING:create_story')
        response = self.client.get(url, data={'story_form': StoryForm()})
        self.assertTemplateUsed(response, 'create_story.html')

    # def test_redirect_to_homepage(self):
    #     self.client.force_login(self.user)
    #     url = reverse('TELLING:create_story')
    #     url_redirect = reverse('TELLING:homepage')
    #     response = self.client.post(url, data={'story_form': StoryForm()}, follow=True)
    #     self.assertRedirects(response, url_redirect, status_code=302)
