from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Testimonial
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm, EditTestimonialForm


def testimonial_list_view(request):
    testimonials = Testimonial.objects.all()
    return render(
        request, 'testimonial/testimonial.html', {'testimonials': testimonials}
    )


def testimonial_detail_view(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    testimonial_form = TestimonialForm()
    return render(request, 'testimonial/testimonial-details.html', {
        'testimonial': testimonial,
        'testimonial_form': testimonial_form
    })


@login_required
def new_testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            return redirect('testimonial')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial/new-testimonial.html', {
        'form': form})


@login_required
def edit_testimonial_view(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        form = EditTestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully')
            return redirect('testimonial-detail', id=id)
    else:
        form = EditTestimonialForm(instance=testimonial)
    return render(request, 'testimonial/edit-testimonial.html', {
        'form': form})


@login_required
def delete_testimonial_view(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully')
        return redirect('testimonial')
    return render(request, 'testimonial/delete-testimonial.html', {
        'testimonial': testimonial})
