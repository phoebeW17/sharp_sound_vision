from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from testimonial.models import Testimonial

class TestimonialViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.testimonial = Testimonial.objects.create(
            user=self.user,
            title='Test Title',
            text='Test testimonial text',
            project_type='brand_videos',
            status=1
        )

    def test_testimonial_list_view(self):
        response = self.client.get(reverse('testimonial'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')

    def test_testimonial_detail_view(self):
        response = self.client.get(reverse('testimonial-detail', args=[self.testimonial.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')

    def tearDown(self):
        self.user.delete()
        self.testimonial.delete()