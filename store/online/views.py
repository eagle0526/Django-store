from django.shortcuts import render
from django.http import HttpResponse
from .models import Employer, Store, Product
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
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


from django.contrib.auth.mixins import LoginRequiredMixin

class EmployerListView(LoginRequiredMixin, generic.ListView):
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


from django.contrib.auth.mixins import PermissionRequiredMixin


class StoreListView(PermissionRequiredMixin, generic.ListView):
    model = Store
    permission_required = ('online.can_mark_store')    
    raise_exception = True  # 如果用戶沒有權限，引發PermissionDenied異常    

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
