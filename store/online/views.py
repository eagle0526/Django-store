from django.shortcuts import render
from django.http import HttpResponse
from .models import Employer
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request, "index.html")



class EmployerListView(generic.ListView):
    model = Employer

class EmployerCreate(CreateView):
    model = Employer
    fields = '__all__'
    success_url = reverse_lazy('employer-list')

class EmployerDetailView(generic.DetailView):
    model = Employer

class EmployerUpdate(UpdateView):
    model = Employer
    fields = '__all__'

