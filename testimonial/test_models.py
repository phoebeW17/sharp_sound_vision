from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from testimonial.models import Testimonial

class TestimonialModelTest(TestCase):

    def setUp(self):
        # Create a user to associate with the testimonials
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.testimonial = Testimonial.objects.create(
            user=self.user,
            title='Test Title',
            text='Test testimonial text',
            project_type='brand_videos',
            status=1
        )

    def test_create_testimonial(self):
        # Test creating a testimonial
        self.assertEqual(self.testimonial.title, 'Test Title')
        self.assertEqual(self.testimonial.text, 'Test testimonial text')
        self.assertEqual(self.testimonial.project_type, 'brand_videos')
        self.assertEqual(self.testimonial.status, 1)

    def test_testimonial_str(self):
        # Test the string representation of a testimonial
        self.assertEqual(str(self.testimonial), f"{self.testimonial.title} | written by {self.user}")

    def test_testimonial_ordering(self):
        # Test the ordering of testimonials
        testimonial1 = Testimonial.objects.create(
            user=self.user,
            title='Another Test Title',
            text='Another test testimonial text',
            project_type='explainer_videos',
            status=1
        )
        testimonials = Testimonial.objects.all()
        self.assertEqual(testimonials[0], testimonial1)
        self.assertEqual(testimonials[1], self.testimonial)

    def test_testimonial_project_type_choices(self):
        # Test the project type choices for a testimonial
        self.assertEqual(self.testimonial.get_project_type_display(), 'Brand Videos')

    def test_testimonial_status_choices(self):
        # Test the status choices for a testimonial
        self.assertEqual(self.testimonial.get_status_display(), 'Published')

    def test_create_testimonial_without_title(self):
        # Test creating a testimonial without a title
        testimonial = Testimonial(
            user=self.user,
            text='Test testimonial text',
            project_type='brand_videos',
            status=1
        )
        with self.assertRaises(ValidationError):
            testimonial.full_clean()  # This will raise a ValidationError

    def tearDown(self):
        # Clean up after each test
        self.user.delete()
        self.testimonial.delete()