from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Testimonial
from django.contrib.auth.decorators import login_required

# class TestimonialList(generic.ListView):
#     queryset = Testimonial.objects.filter(status=1).order_by('-posted_on')
#     template_name = 'testimonial/testimonial.html'
from django.contrib.auth.decorators import login_required

# class TestimonialList(generic.ListView):
#     queryset = Testimonial.objects.filter(status=1).order_by('-posted_on')
#     template_name = 'testimonial/testimonial.html'

def testimonial_list_view(request):
    testimonials = Testimonial.objects.all()

    return render(request, 'testimonial/testimonial.html', {
        'testimonials': testimonials
    })

def testimonial_detail_view(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    return render(request, 'testimonial/testimonial-details.html', {'testimonial': testimonial})