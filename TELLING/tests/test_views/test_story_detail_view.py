from django.test import TestCase
from django.urls import reverse


class StoryDetailTest(TestCase):
    def test_can_access_by_url_name(self):
        """
        Test that a view can be access using url name
        """
        url = reverse('TELLING:detail')
        response = self.client.post(url, data={'story': 1})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `story_detail.html`
        """
        url = reverse('TELLING:detail')
        response = self.client.post(url, data={'story': 1})
        self.assertTemplateUsed(response, 'TELLING/story_detail.html')
