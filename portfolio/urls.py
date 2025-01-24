from django.urls import path
from portfolio.views import portfolio_view, like_portfolio

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('portfolio/like/<int:id>/', like_portfolio, name='like_portfolio'),
]
