from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_view, name='testimonial'),
    path('<slug:slug>/', views.testimonial_detail, name='testimonial_detail'),
    path('testimonial/<int:id>/', views.testimonial_detail, name='testimonial-detail'),


    ]