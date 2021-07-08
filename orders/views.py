from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Customer
from products.models import Product
from .models import Order
from .forms import *



def order_list(request):
    orders = Order.objects.all()
    all_orders = orders.count()

    pending = orders.filter(status='Pending')
    out_for_delivery = orders.filter(status='Out for delivery')
    delivered = orders.filter(status='Delivered')

    context = {
        'orders': orders,
        'all_orders': all_orders,
        'pending': pending,
        'out_for_delivery': out_for_delivery,
        'delivered': delivered,
    }
    return render(request, 'customer/customer-home.html', context)


# def admin_order(request):
#     customers = Customer.objects.all()
#     products = Product.objects.all()
#
#     if request.user.is_authenticated and request.user.is_superuser:
#         if request.method == 'POST':
#             form = AdminOrderForm(request.POST, request.FILES)
#             if form.is_valid():
#                 return redirect('dashboard')
#         else:
#             form = AdminOrderForm()
#
#         context = {
#             'form': form,
#             'products': products,
#             'customers': customers
#         }
#         return render(request, 'admin/add-order.html', context)


def create_customer_order(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    if request.user.is_authenticated:
        Order.objects.create(
            customer=request.user.customer,
            product=product,
            status='Pending',
        )
        return redirect('products_list')

    return render(request, 'products/products-list.html')


def customer_orders(request, id):
    customer = get_object_or_404(Customer, id=id)
    orders = customer.order_set.all()



    context = {
        'customer': customer,
        'orders': orders
    }
    return render(request, 'customer/customer-orders.html', context)






















