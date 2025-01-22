from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.testimonial_list_view, name='testimonial'),
    path('<int:id>/', views.testimonial_detail_view, name='testimonial-detail'),
    path('new/', views.new, name='new-testimonial'),
    path('edit-testimonial/<int:id>/', views.edit, name='edit-testimonial'),
    path('delete-testimonial/<int:id>/', views.delete, name='delete-testimonial'),
]