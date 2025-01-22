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

    return render(request, 'testimonial/testimonial-details.html', {
        'testimonial': testimonial
    })

def new_testimonial_view(request):
    return render(request, 'testimonial/new-testimonial.html')

@login_required
def new(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)

        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.success(request, 'Testimonial created successfully')

            return redirect('testimonial:testimonial_list')
    else:
        form = TestimonialForm()

    return render(request, 'testimonial/new.html', {
        'form': form,
        'title': 'New Testimonial'
    })

@login_required
def edit(request, id):
    testimonial = get_object_or_404(Testimonial, id=id, author=request.user)

    if request.method == 'POST':
        form = EditTestimonialForm(request.POST, instance=testimonial)

        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.save()
            messages.success(request, 'Testimonial updated successfully')

            return redirect('testimonial:testimonial_list')
    else:
        form = EditTestimonialForm(instance=testimonial)

    return render(request, 'testimonial/edit.html', {
        'form': form,
        'title': 'Edit Testimonial'
    })

@login_required
def delete(request, id):
    testimonial = get_object_or_404(Testimonial, id=id, author=request.user)

    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully')

        return redirect('testimonial:testimonial_list')

    return render(request, 'testimonial/delete.html', {
        'testimonial': testimonial
    })