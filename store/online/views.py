from django.shortcuts import render
from django.http import HttpResponse
from .models import Employer
from django.views import generic
# Create your views here.


def index(request):
    return render(request, "index.html")



class EmployerListView(generic.ListView):
    model = Employer
