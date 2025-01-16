from django.shortcuts import render
from .models import Testimonial

def testimonial_view(request):
    testimonials = Testimonial.objects.filter(status=1).order_by('-posted_on')
    return render(request, 'testimonial/testimonial.html', {'testimonials': testimonials})
