from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testimonial.models import Testimonial

@login_required
def user_dashboard_view(request):
    user_testimonials = Testimonial.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'testimonials': user_testimonials})
