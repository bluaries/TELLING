from django.test import TestCase
from django.urls import reverse


class StoryDetailTest(TestCase):
    def test_can_access_by_url_name(self):
        """
        Test that a view can be access using url name
        """
        url = reverse('TELLING:detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `story_detail.html`
        """
        url = reverse('TELLING:detail')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'quizer_game/story_detail.html')
