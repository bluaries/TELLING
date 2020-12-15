from django.test import TestCase
from django.urls import reverse
from TELLING.models import Story


class StoryDetailTest(TestCase):
    def test_can_access_by_url_name(self):
        """
        Test that a view can be access using url name
        """
        url = reverse('TELLING:detail')

        story = Story.objects.get(1)
        response = self.client.post(url, data={'story': story})
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that a view renders `story_detail.html`
        """
        url = reverse('TELLING:detail')
        story = Story.objects.get(1)
        response = self.client.post(url, data={'story': story})
        self.assertTemplateUsed(response, 'story_detail.html')
