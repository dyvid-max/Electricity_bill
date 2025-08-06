from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<str:customer_id>/', views.customer_detail, name='customer_detail'),
    path('bills/<str:bill_number>/', views.bill_detail, name='bill_detail'),
]