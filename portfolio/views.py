from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Likes


def portfolio_view(request):
    portfolio = Portfolio.objects.filter(status=1).order_by('-id')
    return render(
        request, 'portfolio/portfolio.html', {'portfolio': portfolio}
    )


def like_portfolio(request, id):
    user = request.user
    portfolio = Portfolio.objects.get(id=id)
    current_likes = portfolio.likes
    liked = Likes.objects.filter(user=user, portfolio=portfolio).count()
    if not liked:
        like = Likes.objects.create(user=user, portfolio=portfolio)
        current_likes = current_likes + 1
    else:
        liked = Likes.objects.filter(user=user, portfolio=portfolio).delete()
        current_likes = current_likes - 1

    portfolio.likes = current_likes
    portfolio.save()
    return HttpResponseRedirect('/portfolio')
