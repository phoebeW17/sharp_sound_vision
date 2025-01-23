from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Portfolio

def portfolio_view(request):
    portfolio = Portfolio.objects.filter(status=1).order_by('-id')
    return render(request, 'portfolio/portfolio.html', {'portfolio': portfolio})

def like_portfolio(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    portfolio.likes += 1
    portfolio.save()
    return JsonResponse({'likes': portfolio.likes})
