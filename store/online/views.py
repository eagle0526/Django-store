from django.shortcuts import render
from django.http import HttpResponse
from .models import Employer, Store, Product
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    num_employers = Employer.objects.all()
    num_stores = Store.objects.all()
    num_products = Product.objects.all()

    context = {
        "num_employers": num_employers,
        "num_stores": num_stores,
        "num_products": num_products,
    }

    return render(request, 'index.html', context=context)




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

class EmployerDelete(DeleteView):
    model = Employer
    success_url = reverse_lazy('employer-list')




class StoreListView(generic.ListView):
    model = Store

class StoreCreate(CreateView):
    model = Store
    fields = '__all__'
    success_url = reverse_lazy('store-list')

class StoreDetailView(generic.DetailView):
    model = Store    

class StoreUpdate(UpdateView):
    model = Store
    fields = "__all__"

class StoreDelete(DeleteView):
    model = Store
    success_url = reverse_lazy('store-list')    


class ProductListView(generic.ListView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductDetailView(generic.DetailView):
    model = Product    

class ProductUpdate(UpdateView):
    model = Product
    fields = "__all__"    

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product-list')    
