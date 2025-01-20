from django.urls import path, include

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('sharpsound')
]
