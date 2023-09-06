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
]

