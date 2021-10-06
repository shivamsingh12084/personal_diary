
from django.views.generic import TemplateView
from django.shortcuts import render
from . models import Topic


class HomePageView(TemplateView):
    template_name = 'home.html'


def index(request):
    return render(request, "main_home.html", {
        "topics": Topic.objects.all()
    })