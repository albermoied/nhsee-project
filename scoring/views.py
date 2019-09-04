from django.shortcuts import render
from django.views.generic import ListView
from scoring.models import Project
#from .forms import ProjectForm

class HomePageView(ListView):

    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'home.html', locals())
