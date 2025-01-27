from django.urls import path
from .views import user_dashboard_view
from testimonial.views import (
    EditTestimonialForm,
    delete_testimonial_view,
    edit_testimonial_view
)

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', user_dashboard_view, name='user_dashboard'),
    path(
        'testimonial/edit/<int:id>/',
        edit_testimonial_view,
        name='edit_testimonial'
    ),
    path(
        'testimonial/delete/<int:id>/',
        delete_testimonial_view,
        name='delete_testimonial'
    ),
]
