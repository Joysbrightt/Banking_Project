from django.urls import path
from . import views

urlpatterns = [
    path("customer/", views.customer),
    path("create/", views.createCustomer),
]