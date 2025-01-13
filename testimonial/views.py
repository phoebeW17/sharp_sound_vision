from django.shortcuts import render

def testimonial_view(request):
    return render(request, 'testimonial/testimonial.html')
