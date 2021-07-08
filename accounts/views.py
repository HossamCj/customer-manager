from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages

from orders.models import Order
from .forms import *


@login_required(login_url='login_all')
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request, 'admin/dashboard.html', context)


def signup_admin(request):
    if request.method == 'POST':
        admin_form = SignUpUserForm(request.POST)
        if admin_form.is_valid():
            request.user.is_staff = True
            user = admin_form.save()
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            user.is_staff = True
            user.save()

            return redirect('login_admin')
    else:
        admin_form = SignUpUserForm()

    context = {'admin_form': admin_form}
    return render(request, 'registration/admin-registration.html', context)


def signup_customer(request):
    if request.method == 'POST':
        user_form = SignUpUserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data.get('username')
            email = user_form.cleaned_data.get('email')
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Customer.objects.create(
                user=user,
                name=username,
                email=email,
            )

            return redirect('login_all')
    else:
        user_form = SignUpUserForm()

    context = {'user_form': user_form}
    return render(request, 'registration/customer-registration.html', context)


def login_all(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.groups.filter(name='customer'):
            login(request, user)
            return redirect('products_list')

        elif user is not None and user.groups.filter(name='admin'):
            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login_all')

    return render(request, 'registration/login.html')


def logout_all(request):
   logout(request)
   return redirect('login_all')


@login_required(login_url='login_all')
def customer_home(request, id):
    customer = get_object_or_404(Customer, id=id)

    orders = request.user.customer.order_set.all()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered')
    pending = orders.filter(status='Pending')
    out_for_delivery = orders.filter(status='Out for delivery')

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'pending': pending,
        'out_for_delivery': out_for_delivery,
    }
    return render(request, 'customer/customer-home.html', context)


def customer_settings(request, id):
    customer = get_object_or_404(Customer, id=id)
    form = SignUpCustomerForm(instance=customer)

    if request.method == 'POST':
        form = SignUpCustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_settings_edited')
    context = {
        'customer': customer,
        'form': form,
       }
    return render(request, 'customer/customer-settings.html', context)


def customer_settings_edited(request):
    return render(request, 'customer/edited-settings.html')


def client(request, id):
    client = get_object_or_404(Customer, id=id)
    orders = client.order_set.all()
    order_count = orders.count()

    context = {
        'client': client,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'admin/client.html', context)




















