from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list_view, name='testimonial'),
    path('<int:id>/', views.testimonial_detail_view, name='testimonial-detail'),
    path('new/', views.new_testimonial_view, name='new-testimonial'),
    path('edit/<int:id>/', views.edit_testimonial_view, name='edit-testimonial'),
    path('delete/<int:id>/', views.delete_testimonial_view, name='delete-testimonial'),
]