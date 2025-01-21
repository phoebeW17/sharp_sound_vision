from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list_view, name='testimonial'),
    path('<int:id>/', views.testimonial_detail_view, name='testimonial-detail'),
]