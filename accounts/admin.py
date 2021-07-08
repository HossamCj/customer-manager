from django.contrib import admin, auth
from django.contrib.auth.models import User

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone', 'email', 'created_at')
    list_filter = ('user', 'phone', 'email')
    list_editable = ('phone', 'name')


admin.site.register(Customer, CustomerAdmin)