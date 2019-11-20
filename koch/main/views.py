from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings

from django.views.generic import TemplateView
from django.views import generic

from .models import Playground


def handler404(request, exception):
    # data = {"name": "ThePythonDjango.com"}
    return render(request,'errors/404.html')


def handler500(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'errors/404.html')


def index(request):
    return render(request, 'main/index.html')


class PlaygroundView(generic.ListView):
    template_name = 'main/playgrounds.html'
    context_object_name = 'list_playground'

    def get_queryset(self):
        return Playground.objects.all()