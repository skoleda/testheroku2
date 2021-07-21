from django.urls import path
from .views import HomePageViews, AboutViews

urlpatterns = [
    path('', HomePageViews.as_view(), name='home'),
    path('about/', AboutViews.as_view(), name='about'),
]
