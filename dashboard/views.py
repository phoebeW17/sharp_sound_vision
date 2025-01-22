from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from testimonial.models import Testimonial

@login_required
def dashboard(request):
    testimonials = Testimonial.objects.filter(author=request.user)

    return render(request, 'dashboard/dashboard.html', {
        'testimonials': testimonials,
        })
