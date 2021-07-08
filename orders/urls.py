from django.urls import path

from .views import *


urlpatterns = [
    path('customer-orders/<int:id>/', customer_orders, name='customer_orders'),
    path('create-customer-order/<int:id>/<slug>/', create_customer_order, name='create_customer_order'),
]