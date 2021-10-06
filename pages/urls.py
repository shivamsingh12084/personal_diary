from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("main_homepage/", views.index, name='main_home')
]