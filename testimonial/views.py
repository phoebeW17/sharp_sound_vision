from django.shortcuts import render
from django.views import generic
from .models import Testimonial

class TestimonialList(generic.ListView):
    queryset = Testimonial.objects.filter(status=1).order_by('-posted_on')
    template_name = 'testimonial/testimonial.html'

def testimonial_view(request):
    testimonials = Testimonial.objects.filter(status=1).order_by('-posted_on')
    return render(request, 'testimonial/testimonial.html', {'testimonials': testimonials})

def testimonial_detail(request, slug):
    queryset = Testimonial.objects.filter(status=1).order_by('-posted_on')