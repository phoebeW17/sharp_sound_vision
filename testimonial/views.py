from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Testimonial
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

def new_testimonial_view(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'testimonial/new-testimonial.html')

def edit(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'testimonial/edit-testimonial.html', {'testimonial': testimonial})

def delete(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial')
    return render(request, 'testimonial/delete-testimonial.html', {'testimonial': testimonial})