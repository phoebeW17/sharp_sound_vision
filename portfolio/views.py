from django.shortcuts import render
from .models import Portfolio

def portfolio_view(request):
    portfolio = Portfolio.objects.filter(status=1).order_by('-id')
    return render(request, 'portfolio/portfolio.html', {'portfolio': portfolio})
