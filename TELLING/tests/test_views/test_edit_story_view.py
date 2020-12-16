from django.test import TestCase
from django.urls import reverse
from TELLING.models import Story, Category
from TELLING.forms import StoryForm
from django.contrib.auth.models import User


class EditStoryTest(TestCase):
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
        url = reverse('TELLING:edit_story', kwargs={'pk': 1})
        self.client.force_login(self.user)

        story = Story.objects.get(pk=1)
        response = self.client.get(url, data={'update_story_form': StoryForm(instance=story)})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `edit_story.html`
        """
        url = reverse('TELLING:edit_story', kwargs={'pk': 1})
        self.client.force_login(self.user)

        story = Story.objects.get(pk=1)
        response = self.client.get(url, data={'update_story_form': StoryForm(instance=story)})
        self.assertTemplateUsed(response, 'edit_story.html')
