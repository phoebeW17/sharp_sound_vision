from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testimonial(request):
    return HttpResponse('<h1>Testimonial Home</h1>')