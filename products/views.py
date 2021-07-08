from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import AddProductForm


def products_list(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'products/products-list.html', context)


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'products/product-details.html', context)


def product_add(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('products_list')
        else:
            form = AddProductForm()

        context = {
            'form': form,
            'operation': 'Add product',
        }
        return render(request, 'products/product-add-edit.html', context)


def product_edit(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    form = AddProductForm(instance=product)

    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES, instance=product)

            if form.is_valid():
                form.save()
                return render(request, 'products/product-details.html', {'product': product})
        else:
            form = AddProductForm(instance=product)

        context = {
            'form': form,
            'product': product,
            'operation': 'Edit'
        }
        return render(request, 'products/product-add-edit.html', context)


def product_delete(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    if request.user.is_authenticated and request.user.is_staff:
        product.delete()

        context = {
            'product': product,
            'operation': 'Delete',
        }
        return redirect('products_list')















