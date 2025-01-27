from django.shortcuts import render
from .models import Service


def services_view(request):
    services = Service.objects.filter(status=1).order_by('-id')
    return render(request, 'services/services.html', {'services': services})
