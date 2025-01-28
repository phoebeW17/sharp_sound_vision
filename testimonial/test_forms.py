from django.test import TestCase
from testimonial.forms import TestimonialForm, EditTestimonialForm
from testimonial.models import Testimonial
from django.contrib.auth.models import User

class TestimonialFormTest(TestCase):

    def setUp(self):
        # Create a user to associate with the testimonials
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_valid_testimonial_form(self):
        # Test a valid testimonial form
        form_data = {
            'title': 'Test Title',
            'text': 'Test testimonial text',
            'project_type': 'brand_videos',
            'status': 1
        }
        form = TestimonialForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_testimonial_form(self):
        # Test an invalid testimonial form
        form_data = {
            'title': '',  # Title is required
            'text': 'Test testimonial text',
            'project_type': 'brand_videos',
            'status': 1
        }
        form = TestimonialForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_testimonial_form_missing_fields(self):
        # Test a testimonial form with missing fields
        form_data = {
            'text': 'Test testimonial text',
            'project_type': 'brand_videos',
            'status': 1
        }
        form = TestimonialForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def tearDown(self):
        # Clean up after each test
        self.user.delete()


class EditTestimonialFormTest(TestCase):

    def setUp(self):
        # Create a user and a testimonial to edit
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.testimonial = Testimonial.objects.create(
            user=self.user,
            title='Test Title',
            text='Test testimonial text',
            project_type='brand_videos',
            status=1
        )

    def test_valid_edit_testimonial_form(self):
        # Test a valid edit testimonial form
        form_data = {
            'title': 'Updated Title',
            'text': 'Updated testimonial text',
            'project_type': 'explainer_videos',
            'status': 1
        }
        form = EditTestimonialForm(data=form_data, instance=self.testimonial)
        self.assertTrue(form.is_valid())

    def test_invalid_edit_testimonial_form(self):
        # Test an invalid edit testimonial form
        form_data = {
            'title': '',  # Title is required
            'text': 'Updated testimonial text',
            'project_type': 'explainer_videos',
            'status': 1
        }
        form = EditTestimonialForm(data=form_data, instance=self.testimonial)
        self.assertFalse(form.is_valid())

    def test_edit_testimonial_form_missing_fields(self):
        # Test an edit testimonial form with missing fields
        form_data = {
            'text': 'Updated testimonial text',
            'project_type': 'explainer_videos',
            'status': 1
        }
        form = EditTestimonialForm(data=form_data, instance=self.testimonial)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def tearDown(self):
        # Clean up after each test
        self.user.delete()
        self.testimonial.delete()