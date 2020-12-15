from django.test import TestCase
from django.urls import reverse


class CreateStoryTest(TestCase):
    def test_can_access_by_url_name(self):
        """
        Test that a view can be access using url name
        """
        url = reverse('TELLING:create_story')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `create_story.html`
        """
        url = reverse('TELLING:create_story')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'create_story.html')
