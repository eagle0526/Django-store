from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index")
]


urlpatterns += [
    path("employers/", views.EmployerListView.as_view(), name='employer-list'),
    path("employer/create/", views.EmployerCreate.as_view(), name='employer-create'),
    path("employer/<int:pk>/", views.EmployerDetailView.as_view(), name='employer-detail'),
    path("employer/<int:pk>/update/", views.EmployerUpdate.as_view(), name='employer-update'),
    path("employer/<int:pk>/delete/", views.EmployerDelete.as_view(), name='employer-delete'),
]




urlpatterns += [
    path("stores/", views.StoreListView.as_view(), name='store-list'),
    path("store/create/", views.StoreCreate.as_view(), name='store-create'),    
    path("store/<int:pk>", views.StoreDetailView.as_view(), name="store-detail"),
    path("store/<int:pk>/update/", views.StoreUpdate.as_view(), name="store-update"),    
    path("store/<int:pk>/delete/", views.StoreDelete.as_view(), name="store-delete"), 
]

urlpatterns += [
    path("products/", views.ProductListView.as_view(), name='product-list'),
    path("product/create/", views.ProductCreate.as_view(), name='product-create'),    
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    path("product/<int:pk>/update/", views.ProductUpdate.as_view(), name="product-update"),   
    path("product/<int:pk>/delete/", views.ProductDelete.as_view(), name="product-delete"),  
]






