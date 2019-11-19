from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings


# 


def handler404(request, exception):
    return render(request,'errors/404.html', status = 404)


def handler500(request, exception):
    return render(request,'errors/404.html', status = 500)


def index(request):
    return render(request, 'main/index.html', {})
