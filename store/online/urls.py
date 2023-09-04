from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index")
]




urlpatterns += [
    path("employers/", views.EmployerListView.as_view(), name='employer-list')
]


