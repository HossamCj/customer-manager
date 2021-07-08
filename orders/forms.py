from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):
    model = Order
    fields = '__all__'