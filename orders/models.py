from django.db import models
from django.urls import reverse

from accounts.models import Customer
from products.models import Product


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery '),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title