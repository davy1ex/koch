from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic import TemplateView
from django.views import generic

from .models import Playground
from .forms import PlaygroundForm


def handler404(request, exception):
    # data = {"name": "ThePythonDjango.com"}
    return render(request,'errors/404.html')


def handler500(request):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'errors/404.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect(index)


def index(request):
    return render(request, 'main/index.html')


class PlaygroundView(generic.ListView):
    template_name = 'main/playgrounds.html'
    context_object_name = 'list_playground'
    form_class = PlaygroundForm
    

    def get_queryset(self):
        return Playground.objects.all()

def basketball(request):
    p = Playground.objects.filter(playground_type='b')
    form = PlaygroundForm()
    
    if request.method == "POST":
        form = PlaygroundForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            playground = form.save(commit=False)
            # playground_type = request.id_playground_type
            
            # rating = request.rating
            # description = request.id_description
            # latitude = request.id_latitude
            # longitude = request.id_longitude
            # photo = request.id_photo
            playground.save()
        
            return redirect('/')

    return render(request, 'main/playgrounds.html', {'list_playground':p, 'form':form})
        