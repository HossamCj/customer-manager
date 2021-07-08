from django.urls import path

from .views import *


urlpatterns = [
    path('', products_list, name='products_list'),
    path('add-product/', product_add, name='product_add'),
    path('products/<slug>/<int:id>/', product_details, name='product_details'),

    path('edit-product/<slug>/<int:id>/', product_edit, name='product_edit'),
    path('delete-product/<slug>/<int:id>/', product_delete, name='product_delete'),
]